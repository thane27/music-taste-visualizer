import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time

SCOPE = "user-top-read"

def get_spotify_client():
    auth_manager = SpotifyOAuth(
        client_id=st.secrets["SPOTIPY_CLIENT_ID"],
        client_secret=st.secrets["SPOTIPY_CLIENT_SECRET"],
        redirect_uri=st.secrets["SPOTIPY_REDIRECT_URI"],
        scope=SCOPE,
        cache_path=".spotify_cache"
    )
    return spotipy.Spotify(auth_manager=auth_manager)

def get_top_tracks(sp, time_range="medium_term", limit=50):
    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    print(f"Raw API returned {len(results['items'])} tracks")
    tracks = []
    for item in results["items"]:
        tracks.append({
            "id": item["id"],
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "artist_id": item["artists"][0]["id"],
            "album": item["album"]["name"],
            "album_id": item["album"]["id"],
            "release_year": int(item["album"]["release_date"][:4]),
            "explicit": int(item["explicit"]),
            "duration_ms": item["duration_ms"],
        })
    return pd.DataFrame(tracks)

def get_artist_features(sp, artist_ids):
    artist_data = []
    for artist_id in artist_ids:
        try:
            artist = sp.artist(artist_id)
            # genres field removed in Feb 2026, use followers as proxy
            artist_data.append({
                "artist_id": artist["id"],
                "genres": [],
                "num_genres": 0,
            })
            time.sleep(0.1)
        except Exception as e:
            print(f"Failed to fetch artist {artist_id}: {e}")
            artist_data.append({
                "artist_id": artist_id,
                "genres": [],
                "num_genres": 0,
            })
    return pd.DataFrame(artist_data)

def encode_genres(df):
    # Collect all unique genres
    all_genres = set()
    for genres in df["genres"]:
        all_genres.update(genres)

    # Top 10 most common genres only
    from collections import Counter
    genre_counts = Counter(g for genres in df["genres"] for g in genres)
    top_genres = [g for g, _ in genre_counts.most_common(10)]

    # Binary encode top genres
    for genre in top_genres:
        df[f"genre_{genre.replace(' ', '_')}"] = df["genres"].apply(
            lambda x: 1 if genre in x else 0
        )
    return df, top_genres

def get_full_track_data(sp):
    tracks_df = get_top_tracks(sp, time_range="short_term", limit=50)

    # Get unique artist IDs
    unique_artist_ids = tracks_df["artist_id"].unique().tolist()
    artists_df = get_artist_features(sp, unique_artist_ids)

    # Merge
    df = pd.merge(tracks_df, artists_df, on="artist_id", how="left")

    # Engineer features
    df["decade"] = (df["release_year"] // 10) * 10
    df["duration_min"] = df["duration_ms"] / 60000
    df, top_genres = encode_genres(df)

    return df, top_genres
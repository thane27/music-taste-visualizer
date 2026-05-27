import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

FEATURES = [
    "release_year",
    "explicit",
    "duration_min",
]

def generate_cluster_label(cluster_df):
    avg_year = cluster_df["release_year"].mean()
    avg_duration = cluster_df["duration_min"].mean()
    explicit_ratio = cluster_df["explicit"].mean()

    if avg_year < 1995:
        era = "🕰️ Classic"
    elif avg_year < 2015:
        era = "🎸 Throwback"
    else:
        era = "🎵 Modern"

    explicit = "Explicit" if explicit_ratio > 0.5 else "Clean"

    return f"{era} · {explicit}"

def cluster_tracks(df, n_clusters=5):
    X = df[FEATURES].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(X_scaled)

    # Dynamically generate labels based on cluster characteristics
    cluster_labels = {}
    for cluster_id in range(n_clusters):
        cluster_df = df[df["cluster"] == cluster_id]
        cluster_labels[cluster_id] = generate_cluster_label(cluster_df)

    df["cluster_label"] = df["cluster"].map(cluster_labels)

    pca = PCA(n_components=2)
    coords = pca.fit_transform(X_scaled)
    df["pca_x"] = coords[:, 0]
    df["pca_y"] = coords[:, 1]

    return df, scaler, kmeans, pca

def get_taste_fingerprint(df):
    return df[FEATURES].mean().to_dict()
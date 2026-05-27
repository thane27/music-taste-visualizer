from mock_data import get_mock_track_data

df = get_mock_track_data()
print(f"Loaded {len(df)} tracks!")
print(df[["name", "artist", "release_year", "explicit", "duration_min"]].head(10))
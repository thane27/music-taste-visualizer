# 🎵 Music Taste Visualizer

An interactive data science web app that analyzes your Spotify listening history and uses machine learning to uncover hidden patterns in your music taste.

**[Live Demo →](https://music-taste-visualizer-6q5ertplxvtg83uixzuvsv.streamlit.app/?code=AQD7bPawnjW6YkFCbGbamTIbaoBDQyf_GOPYP0MNoXS82mJswno2TuXY3yr8HV-8OIEozOzPgtcoGPWx12HPmvbyVaDzVFYn9hXoKcnh1IYvpvK1FKXjbqSKRWPuQYKGibWoglUaajfXmHtUYpuir9SjhvLAvXE4stMyErl6XAWE2eVASH8jUBJJSTi39UqINAsXJBQajVJWvwSjFBOoDm14Wi0K0ofd1gH-rzVYZqabfThst8wr)**

---

## 🖼️ Overview

Music Taste Visualizer fetches your top Spotify tracks, engineers meaningful features from the data, and applies unsupervised machine learning to cluster your songs into distinct taste groups. The results are presented in an interactive dashboard with four visualizations.

---

## 🔍 How It Works

1. **Data Collection** — Connects to the Spotify Web API via OAuth to fetch your top 50 tracks
2. **Feature Engineering** — Extracts and derives features including release year, duration, and explicit content
3. **ML Clustering** — Applies KMeans clustering with StandardScaler normalization to group songs by similarity
4. **Dimensionality Reduction** — Uses PCA to reduce features to 2D for visualization
5. **Dynamic Labeling** — Automatically generates descriptive cluster labels based on each group's characteristics

---

## 📊 Visualizations

- **Music Taste Map** — 2D scatter plot of all songs colored by cluster, powered by PCA
- **Music by Decade** — Bar chart showing the distribution of your listening across decades
- **Top Artists** — Horizontal bar chart of your most listened to artists
- **Music Breakdown** — Donut chart showing the proportion of each taste cluster

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Dashboard | Streamlit |
| Spotify Integration | Spotipy |
| Machine Learning | Scikit-learn (KMeans, PCA, StandardScaler) |
| Visualizations | Plotly |
| Data Processing | Pandas, NumPy |

---

## 🚀 Running Locally

### Prerequisites
- Python 3.9+
- Spotify Premium account
- Spotify Developer app ([create one here](https://developer.spotify.com/dashboard))

### Setup

1. Clone the repo
```bash
git clone https://github.com/thane27/music-taste-visualizer.git
cd music-taste-visualizer
```

2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add your Spotify credentials — create `.streamlit/secrets.toml`:
```toml
SPOTIPY_CLIENT_ID = "your_client_id"
SPOTIPY_CLIENT_SECRET = "your_client_secret"
SPOTIPY_REDIRECT_URI = "http://localhost:8501"
```

5. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure
music-taste-visualizer/
├── app.py                  # Main Streamlit dashboard
├── spotify_client.py       # Spotify API authentication and data fetching
├── clustering.py           # KMeans clustering and PCA logic
├── visualizations.py       # Plotly chart functions
├── mock_data.py            # Demo dataset of 100 real popular tracks
├── requirements.txt        # Dependencies
└── .streamlit/
└── secrets.toml        # Credentials (never committed to GitHub)

---

## ⚠️ Note on Spotify API

In February 2026 Spotify restricted several API endpoints for Development Mode apps, including the audio features endpoint. This app uses feature engineering from available endpoints (track metadata, artist data) as an alternative. The live demo runs on a curated dataset of 100 real popular tracks.

---

## 📝 License

MIT
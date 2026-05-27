import streamlit as st
from clustering import cluster_tracks, get_taste_fingerprint
from visualizations import plot_scatter, plot_decade_distribution, plot_top_artists, plot_cluster_breakdown
from mock_data import get_mock_track_data

# --- Page Config ---
st.set_page_config(
    page_title="Music Taste Visualizer",
    page_icon="🎵",
    layout="wide"
)

# --- Header ---
st.title("🎵 Music Taste Visualizer")
st.markdown("Discover the hidden patterns in your music taste using AI clustering.")
st.divider()
st.info("🎵 **Demo Mode** — Showing sample data. Connect your Spotify account to visualize your own music taste.")


# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    n_clusters = st.slider("Number of Clusters", min_value=2, max_value=5, value=3)
    st.divider()
    st.markdown("### About")
    st.markdown(
        "This app analyzes your Spotify listening history and uses "
        "machine learning to cluster your songs into taste groups."
    )

# --- Load & Process Data ---
with st.spinner("Fetching your music data..."):
    df = get_mock_track_data()
    df, scaler, kmeans, pca = cluster_tracks(df, n_clusters=n_clusters)

# --- Stats Row ---
col1, col2, col3 = st.columns(3)
col1.metric("🎵 Tracks Analyzed", len(df))
col2.metric("🎨 Clusters Found", n_clusters)
col3.metric("🎤 Unique Artists", df["artist"].nunique())

st.divider()

# --- Charts Row 1 ---
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_scatter(df), use_container_width=True)
with col2:
    st.plotly_chart(plot_decade_distribution(df), use_container_width=True)

# --- Charts Row 2 ---
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_top_artists(df), use_container_width=True)
with col2:
    st.plotly_chart(plot_cluster_breakdown(df), use_container_width=True)

st.divider()

# --- Track Table ---
st.subheader("🎧 Your Tracks")
st.dataframe(
    df[["name", "artist", "album", "release_year", "duration_min", "explicit", "cluster_label"]]
    .sort_values("cluster_label")
    .reset_index(drop=True),
    use_container_width=True
)
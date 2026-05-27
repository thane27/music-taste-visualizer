import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

FEATURES = [
    "release_year",
    "decade", 
    "explicit",
    "duration_min",
    "num_genres",
]

def plot_scatter(df):
    fig = px.scatter(
        df,
        x="pca_x",
        y="pca_y",
        color="cluster_label",
        hover_data=["name", "artist", "release_year", "duration_min", "explicit"],
        title="Your Music Taste Map",
        labels={"pca_x": "Principal Component 1", "pca_y": "Principal Component 2"},
        template="plotly_dark",
    )
    fig.update_traces(marker=dict(size=10, opacity=0.8))
    fig.update_layout(legend_title="Cluster")
    return fig

def plot_decade_distribution(df):
    df = df.copy()
    df["decade"] = (df["release_year"] // 10) * 10
    decade_counts = df.groupby("decade").size().reset_index(name="count")
    decade_counts["decade"] = decade_counts["decade"].astype(str) + "s"

    fig = px.bar(
        decade_counts,
        x="decade",
        y="count",
        title="Your Music by Decade",
        labels={"decade": "Decade", "count": "Number of Tracks"},
        template="plotly_dark",
        color="count",
        color_continuous_scale="Teal",
    )
    fig.update_layout(coloraxis_showscale=False)
    return fig

def plot_top_artists(df):
    top_artists = df["artist"].value_counts().head(10).reset_index()
    top_artists.columns = ["artist", "count"]

    fig = px.bar(
        top_artists,
        x="count",
        y="artist",
        orientation="h",
        title="Your Top Artists",
        labels={"count": "Number of Tracks", "artist": ""},
        template="plotly_dark",
        color="count",
        color_continuous_scale="Teal",
    )
    fig.update_layout(coloraxis_showscale=False, yaxis=dict(autorange="reversed"))
    return fig

def plot_cluster_breakdown(df):
    cluster_counts = df["cluster_label"].value_counts().reset_index()
    cluster_counts.columns = ["cluster_label", "count"]

    fig = px.pie(
        cluster_counts,
        names="cluster_label",
        values="count",
        title="Your Music Breakdown",
        template="plotly_dark",
        hole=0.4,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return fig
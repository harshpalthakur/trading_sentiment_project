"""Shared utility functions used across all notebooks."""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd


COLORS = {
    "Extreme Fear": "#d62728",
    "Fear": "#ff7f0e",
    "Neutral": "#bcbd22",
    "Greed": "#2ca02c",
    "Extreme Greed": "#1f77b4",
}
ZONE_ORDER = ["Extreme Fear", "Fear", "Neutral", "Greed", "Extreme Greed"]


ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
CHARTS_DIR = ROOT / "outputs" / "charts"
REPORTS_DIR = ROOT / "outputs" / "reports"

for directory in (PROCESSED_DIR, CHARTS_DIR, REPORTS_DIR):
    directory.mkdir(parents=True, exist_ok=True)


def save_fig(name: str, dpi: int = 150) -> None:
    """Save the current figure into outputs/charts."""
    path = CHARTS_DIR / f"{name}.png"
    plt.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    print(f"Saved -> {path}")


def style_axes(ax, title: str = "", xlabel: str = "", ylabel: str = "") -> None:
    ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=9)


def zone_color(zone: str) -> str:
    return COLORS.get(zone, "#999999")


def load_processed():
    """Load cleaned datasets from data/processed."""
    fg = pd.read_csv(PROCESSED_DIR / "fear_greed_clean.csv", parse_dates=["date"])
    tr = pd.read_csv(PROCESSED_DIR / "trades_clean.csv", parse_dates=["date", "time"])
    merged = pd.read_csv(PROCESSED_DIR / "merged.csv", parse_dates=["date", "time"])

    if "zone" in fg.columns:
        fg["zone"] = pd.Categorical(fg["zone"], categories=ZONE_ORDER, ordered=True)
    if "zone" in merged.columns:
        merged["zone"] = pd.Categorical(merged["zone"], categories=ZONE_ORDER, ordered=True)
    if "has_sentiment" not in merged.columns and "fgi_score" in merged.columns:
        merged["has_sentiment"] = merged["fgi_score"].notna()

    return fg, tr, merged


def matched_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """Return only rows with a matched Fear & Greed observation."""
    if "has_sentiment" in df.columns:
        return df[df["has_sentiment"]].copy()
    if "fgi_score" in df.columns:
        return df[df["fgi_score"].notna()].copy()
    return df.copy()


def section(title: str) -> None:
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

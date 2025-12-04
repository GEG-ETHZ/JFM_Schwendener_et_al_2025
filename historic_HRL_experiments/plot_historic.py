import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib.colors import LogNorm

# ── Paths ───────────────────────────────────────────────────────────
meta_file = Path("./HRL_historic_experiments.csv")
data_dir = Path("./Data_sets")

# ── Load metadata ───────────────────────────────────────────────────
meta = pd.read_csv(meta_file)
meta.columns = meta.columns.str.strip()

# Clean Pr_p (remove commas, handle NaNs)
meta["Pr_p"] = (
    meta["Pr_p"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .replace("nan", np.nan)
    .astype(float)
)

# Keep only rows with valid Pr_p and Da
meta = meta.dropna(subset=["Pr_p", "Da"])

# ── Color mapping based on Darcy number ─────────────────────────────
valid_da = meta["Da"].astype(float)
norm = LogNorm(vmin=valid_da.min(), vmax=valid_da.max())
cmap = plt.cm.cividis

# ── Marker mapping per author ───────────────────────────────────────
marker_cycle = ["o", "*", "D", "^", "v", "P", "X", "s", "<", ">"]  # swapped "*" and "s"
authors = meta["Name"].unique()
author_marker = {author: marker_cycle[i % len(marker_cycle)] for i, author in enumerate(authors)}

# ── Plot ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 7))

for i, row in meta.iterrows():
    key = str(row["Key"])
    pr_p = row["Pr_p"]
    da = row["Da"]
    author = row["Name"]

    file = data_dir / f"{key}.csv"
    try:
        df = pd.read_csv(file)
        df.columns = df.columns.str.strip()

        # Scaling
        x = df["Ra_D"].values / pr_p
        y = df["Nu"].values / pr_p 

        # Filter out y > 1.5
        mask = y <= 1.5
        x, y = x[mask], y[mask]

        if len(x) == 0:
            continue

        color = cmap(norm(da))
        marker = author_marker.get(author, "o")

        ax.scatter(
            x, y, color=color, s=30, marker=marker,
            edgecolors="black", linewidth=0.2, label=author
        )

    except Exception as e:
        print(f"Skipping {file}: {e}")


# ── Axes formatting ─────────────────────────────────────────────────
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel(r"$Ra_D / Pr_p$", fontsize=14)
ax.set_ylabel(r"$Nu / (Ra_D / Ra_c)$", fontsize=14)
ax.set_title("Historic HRL Experiments: Normalized by $Pr_p$", fontsize=15)

# Equal aspect in log–log space
ax.set_aspect("equal", adjustable="box")
# Add grid
ax.grid(True, which="both", ls="--", alpha=0.2)

# Colorbar for Darcy number
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label(r"$Da$ (log scale)")

# Legend: one entry per author + "This study"
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), fontsize=10, loc="best")

plt.tight_layout()

# Save as SVG locally
#plt.savefig(out_file, format="svg")
plt.show()



"""Figures of Sec. 7.1 (the transfer of Nishino's construction to (11+8n)+3).

Writes fig_transfer.pdf/.png and fig_transfercount.pdf/.png; optional
--output-dir selects the destination.  All numbers are closed formulas:
source (11+4n, 3+4n) with Nishino's rank 4n+2, target (11+8n, 3) with
Witt index 3, allowed rank 2, residual dimension D' = 10+8n, residual
Weyl dimension N = 2^(4+4n) against 2(D'-2) = 16+16n.
"""
import argparse
import os
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--output-dir', type=Path,
                    default=Path(__file__).resolve().parents[2] / 'generated-figures')
OUT = str(parser.parse_args().output_dir)
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.size": 10, "mathtext.fontset": "cm"})
BLUE, RED, GREY, GREEN = "#2b5d9b", "#b8312f", "#7f7f7f", "#2e8b57"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT, name + ".png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_transfer():
    """(s,t,k): Nishino's frames in (11+4n,3+4n) and what is left in (11+8n,3)."""
    fig = plt.figure(figsize=(6.6, 5.4))
    ax = fig.add_subplot(111, projection="3d")
    # Witt wall k = min(s,t) = t over the strip t <= 12
    Sg, Tg = np.meshgrid(np.linspace(10, 28, 10), np.linspace(2, 12, 10))
    ax.plot_surface(Sg, Tg, Tg, color=GREY, alpha=0.10, linewidth=0)
    for n in (0, 1, 2):
        s0, t0, k0 = 11 + 4 * n, 3 + 4 * n, 4 * n + 2
        s1, t1 = 11 + 8 * n, 3
        # source: real frame of Nishino's rank (allowed, below the wall)
        ax.plot([s0, s0], [t0, t0], [0, k0], color=BLUE, lw=2.2)
        ax.scatter([s0], [t0], [k0], color=BLUE, s=40, depthshade=False)
        if n:
            # transfer: 4n timelike directions moved into space
            ax.plot([s0, s1], [t0, t1], [0, 0], color=GREY, lw=1.0, ls="--")
            # target: Nishino's rank is above the Witt index 3
            ax.plot([s1, s1], [t1, t1], [3, k0], color=RED, lw=1.0, ls=":")
            ax.scatter([s1], [t1], [k0], s=46, facecolors="white", edgecolors=RED,
                       linewidths=1.4, depthshade=False)
            ax.plot([s1, s1], [t1, t1], [0, 3], color=GREY, lw=2.2)
            ax.scatter([s1], [t1], [2], color=GREEN, s=70, marker="*", depthshade=False)
            ax.text(s1 + 0.4, t1, k0 + 0.4, f"$({s1},{t1})$", color=RED, fontsize=9)
            ax.text(s0 - 1.2, t0 + 0.6, k0 + 0.6, f"$({s0},{t0})$", color=BLUE, fontsize=9)
        else:
            ax.scatter([s0], [t0], [k0], color=GREEN, s=70, marker="*", depthshade=False)
            ax.text(s0 + 0.6, t0 - 0.2, k0 + 0.9, "$(11,3)$", color=BLUE, fontsize=9)
    ax.scatter([], [], color=BLUE, s=30, label="Nishino's real frame, $k=4n+2$")
    ax.scatter([], [], facecolors="white", edgecolors=RED, s=30, label="the same rank after the transfer")
    ax.scatter([], [], color=GREEN, marker="*", s=50, label="rank allowed by the bracket, $k=2$")
    ax.plot([], [], color=GREY, lw=6, alpha=0.3, label=r"Witt wall $k=\min(s,t)$")
    ax.set_xlabel("$s$"); ax.set_ylabel("$t$"); ax.set_zlabel("$k$")
    ax.set_xlim(10, 28); ax.set_ylim(2, 12); ax.set_zlim(0, 11)
    ax.set_xticks([11, 15, 19, 23, 27]); ax.set_yticks([3, 7, 11]); ax.set_zticks([0, 2, 3, 6, 10])
    ax.view_init(elev=22, azim=-58)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    save(fig, "fig_transfer")


def fig_transfercount():
    """log2 of the residual Weyl dimension against log2 of 2(D'-2), at k = 2."""
    fig = plt.figure(figsize=(6.4, 4.9))
    ax = fig.add_subplot(111, projection="3d")
    ns = np.arange(0, 4)
    N = 2.0 ** (4 + 4 * ns)
    need = 2.0 * (8 + 8 * ns)
    w, y0, y1 = 0.32, 1.6, 0.0
    for i, n in enumerate(ns):
        ax.bar3d(n - w / 2, y1 - w / 2, 0, w, w, np.log2(need[i]), color=BLUE, alpha=0.9, shade=True)
        ax.bar3d(n - w / 2, y0 - w / 2, 0, w, w, np.log2(N[i]), color=RED, alpha=0.9, shade=True)
        ax.text(n, y0, np.log2(N[i]) + 0.8, f"{int(N[i])}", color=RED, fontsize=8, ha="center", zorder=10)
        ax.text(n, y1, np.log2(need[i]) + 0.8, f"{int(need[i])}", color=BLUE, fontsize=8, ha="center", zorder=10)
    ax.set_xticks(ns)
    ax.set_xticklabels(["$11+3$", "$19+3$", "$27+3$", "$35+3$"], fontsize=8)
    ax.set_yticks([y0, y1]); ax.set_yticklabels(["$N$", "$2(D'-2)$"], fontsize=8)
    ax.set_zlabel(r"$\log_2$ of the dimension")
    ax.set_zlim(0, 18); ax.set_zticks([0, 4, 8, 12, 16])
    ax.set_ylim(-0.6, 2.2)
    ax.view_init(elev=24, azim=-30)
    save(fig, "fig_transfercount")


fig_transfer()
fig_transfercount()
print("wrote fig_transfer and fig_transfercount to", OUT)

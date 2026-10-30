"""Figures fig_sharp (Theorems on sufficiency for residual dimension ten and two) and
fig_sources (Theorem on arbitrary contractions of the source).

Run from any directory; --output-dir selects the destination (default: generated-figures
next to the verification folder).
"""
import argparse
import math
import os
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=Path,
                    default=Path(__file__).resolve().parents[2] / "generated-figures")
OUT = str(parser.parse_args().output_dir)
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.size": 10, "mathtext.fontset": "cm"})
BLUE, RED, GREY, GREEN, ORANGE, PURPLE = "#2b5d9b", "#b8312f", "#7f7f7f", "#2e8b57", "#d9822b", "#7b4fa0"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".pdf"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT, name + ".png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


def fig_sharp():
    """(s,t,k) carrying a theory: s+t-2k=10 (Nishino's line and the lines reached by complex
    isometries) and s+t-2k=2 with s=t."""
    fig = plt.figure(figsize=(6.6, 5.4))
    ax = fig.add_subplot(111, projection="3d")
    kmax = 10
    # the plane s+t-2k = 10 over 0 <= k <= kmax, |s-t| <= 10
    K, Dl = np.meshgrid(np.linspace(0, kmax, 21), np.linspace(-10, 10, 21))
    Ssum = 10 + 2 * K
    Sg = (Ssum + Dl) / 2
    Tg = (Ssum - Dl) / 2
    ax.plot_surface(Sg, Tg, K, color=BLUE, alpha=0.10, linewidth=0)
    k = np.arange(0, kmax + 1)
    ax.plot(9 + k, 1 + k, k, color=BLUE, lw=1.2)
    ax.scatter(9 + k, 1 + k, k, color=BLUE, s=22, depthshade=False,
               label=r"Nishino: $(9+k)+(1+k)$")
    ax.plot(5 + k, 5 + k, k, color=GREEN, lw=1.2)
    ax.scatter(5 + k, 5 + k, k, color=GREEN, s=22, depthshade=False,
               label=r"$(5+k)+(5+k)$")
    ax.plot(1 + k, 9 + k, k, color=GREEN, lw=1.2, ls="--")
    ax.scatter(1 + k, 9 + k, k, color=GREEN, s=22, marker="s", depthshade=False,
               label=r"$(1+k)+(9+k)$")
    ax.plot(1 + k, 1 + k, k, color=PURPLE, lw=1.2)
    ax.scatter(1 + k, 1 + k, k, color=PURPLE, s=22, marker="^", depthshade=False,
               label=r"$D'=2$: $(1+k)+(1+k)$")
    ax.scatter([9, 9], [9, 17], [4, 8], color=GREEN, s=95, edgecolor="black",
               linewidth=0.8, depthshade=False, label=r"$9+9$, $9+17$")
    for n in (0, 1, 2):
        s, t = 11 + 8 * n, 3
        ks = np.arange(0, 4)
        ax.plot([s] * 4, [t] * 4, ks, color=RED, lw=1.0)
        ax.scatter([s] * 4, [t] * 4, ks, color=RED, s=14, depthshade=False,
                   label=r"$(11+8n)+3$, $k\leq3$" if n == 0 else None)
    ax.set_xlabel("$s$")
    ax.set_ylabel("$t$")
    ax.set_zlabel("$k$")
    ax.set_xlim(0, 28)
    ax.set_ylim(0, 20)
    ax.set_yticks([0, 5, 10, 15, 20])
    ax.set_zlim(0, kmax)
    ax.view_init(elev=22, azim=-58)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    ax.text2D(0.60, 0.86, r"plane $s+t-2k=10$", color=BLUE, fontsize=9,
              transform=ax.transAxes)
    save(fig, "fig_sharp")


def fig_sources():
    """Bars at (D', p) for p in P', height log10 binom(D', p)."""
    fig = plt.figure(figsize=(6.8, 5.0))
    ax = fig.add_subplot(111, projection="3d")
    for Dp in range(2, 31, 2):
        r = Dp // 2
        P = [p for p in range(r) if (r - p) % 4 == 0]
        if not P:
            ax.bar3d(Dp - 0.4, -0.4, 0, 0.8, 0.8, 0.05, color=GREY, alpha=0.6, shade=True)
            continue
        if len(P) >= 2:
            col = RED
        elif math.comb(Dp, P[0]) <= Dp:
            col = GREEN
        else:
            col = ORANGE
        for p in P:
            h = math.log10(math.comb(Dp, p))
            ax.bar3d(Dp - 0.4, p - 0.4, 0, 0.8, 0.8, max(h, 0.05), color=col, alpha=0.85,
                     shade=True)
    ax.set_xlabel(r"residual dimension $D'$")
    ax.set_ylabel(r"degree $p\in P'$")
    ax.set_zlabel(r"$\log_{10}\binom{D'}{p}$")
    ax.set_xticks(range(2, 31, 4))
    ax.set_yticks(range(0, 15, 2))
    ax.view_init(elev=24, azim=-60)
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in (GREY, GREEN, ORANGE, RED)]
    ax.legend(handles, ["cubic terms vanish", "absorbable", r"needs $k\geq54$",
                        "two degrees: excluded"], loc="upper left", fontsize=8,
              frameon=False)
    save(fig, "fig_sources")


if __name__ == "__main__":
    fig_sharp()
    fig_sources()

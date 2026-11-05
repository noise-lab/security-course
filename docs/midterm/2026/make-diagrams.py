#!/usr/bin/env python3
"""Draw the three diagram figures for the Autumn 2026 midterm (student + solution).

Coordinates are in "data units"; SCALE sets canvas inches per unit, so a smaller
SCALE gives larger type once the figure is printed at a fixed width in the exam.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

OUT = "."
FONT = "Helvetica Neue"
SCALE = 0.55


def box(ax, x, y, w, h, text, fc="#ffffff", ec="#333333", fs=9, lw=1.4, style="round,pad=0.02"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style, fc=fc, ec=ec, lw=lw))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, family=FONT)


def arrow(ax, x0, y0, x1, y1, label="", color="#333333", lw=1.4, style="-|>", ls="-", lx=None, ly=None,
          lcolor=None, fs=8, rad=0.0):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=11, color=color, lw=lw,
                                 linestyle=ls, connectionstyle=f"arc3,rad={rad}"))
    if label:
        ax.text((x0 + x1) / 2 if lx is None else lx, (y0 + y1) / 2 + 0.12 if ly is None else ly, label,
                ha="center", va="bottom", fontsize=fs, family=FONT, color=lcolor or color)


def blank(ax, x, y, w, h, tag):
    ax.add_patch(Rectangle((x, y), w, h, fc="#ffffff", ec="#888888", lw=1.0, ls="--"))
    ax.text(x + 0.05, y + h - 0.05, tag, ha="left", va="top", fontsize=8, family=FONT, color="#888888")


def setup(w, h):
    fig, ax = plt.subplots(figsize=(w * SCALE, h * SCALE))
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    return fig, ax


def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=300, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


# ---------------------------------------------------------------- OAuth roles
def oauth(solution):
    fig, ax = setup(9.6, 4.3)
    labels = {"A": "A", "B": "B", "C": "C", "D": "D"} if not solution else {
        "A": "A: resource owner\n(you)", "B": "B: client\n(the assistant app)",
        "C": "C: authorization server\n(Dropbox login + consent)", "D": "D: resource server\n(Dropbox file API)"}
    lfs = 10 if not solution else 7
    box(ax, 0.2, 1.6, 2.0, 1.0, labels["A"], fc="#fff3cd", fs=lfs)
    box(ax, 3.3, 1.6, 2.2, 1.0, labels["B"], fc="#dbeafe", fs=lfs)
    box(ax, 7.0, 2.95, 2.5, 1.0, labels["C"], fc="#dcfce7", fs=lfs)
    box(ax, 7.0, 0.25, 2.5, 1.0, labels["D"], fc="#fce7f3", fs=lfs)
    arrow(ax, 3.3, 2.35, 2.2, 2.35, "1. asks to access\nyour files", lx=2.75, ly=2.62, fs=8.5)
    arrow(ax, 2.2, 1.85, 3.3, 1.85, "2. you log in at C and approve;\na short-lived grant comes back", lx=2.75, ly=0.95, fs=8.5)
    arrow(ax, 5.5, 2.5, 7.0, 3.35, "", rad=-0.15)
    ax.text(5.2, 3.75, "3. grant + client credentials", ha="center", fontsize=8.5, family=FONT)
    arrow(ax, 7.0, 3.15, 5.5, 2.3, "", rad=-0.15)
    ax.text(8.25, 2.5, "4. scoped access token", ha="center", fontsize=8.5, family=FONT)
    arrow(ax, 5.5, 1.75, 7.0, 1.0, "", rad=0.15)
    ax.text(8.25, 1.55, "5. request + token", ha="center", fontsize=8.5, family=FONT)
    arrow(ax, 7.0, 0.8, 5.5, 1.55, "", rad=0.15)
    ax.text(6.2, 0.02, "6. allowed or denied by scope", ha="center", fontsize=8.5, family=FONT)
    ax.text(4.8, 4.08, "A desktop AI assistant asks to read the files in your Dropbox", ha="center", fontsize=8.5,
            family=FONT, weight="bold")
    save(fig, "oauth-roles-solution" if solution else "oauth-roles")


# ------------------------------------------------------------ DNS lookup trace
def dns(solution):
    fig, ax = setup(9.5, 4.75)
    box(ax, 0.1, 1.7, 2.0, 0.9, "stub resolver\n(your laptop)", fc="#ffffff")
    box(ax, 2.8, 1.7, 2.1, 0.9, "local recursive\nresolver", fc="#dbeafe")
    box(ax, 6.4, 3.5, 2.6, 0.8, "root server", fc="#fff3cd")
    box(ax, 6.4, 1.75, 2.6, 0.8, ".com TLD server", fc="#fff3cd")
    box(ax, 6.4, 0.05, 2.9, 0.8, "authoritative server\nfor foo.com", fc="#dcfce7")
    nfs = 10
    arrow(ax, 2.1, 2.3, 2.8, 2.3, "1", lx=2.45, ly=2.4, fs=nfs)
    arrow(ax, 4.9, 2.5, 6.4, 3.85, "2", lx=5.15, ly=3.45, fs=nfs, rad=-0.15)
    arrow(ax, 6.4, 3.7, 4.9, 2.35, "3", lx=6.05, ly=2.8, fs=nfs, rad=-0.15, color="#2563eb")
    arrow(ax, 4.9, 2.15, 6.4, 2.15, "4", lx=5.65, ly=2.25, fs=nfs)
    arrow(ax, 6.4, 1.95, 4.9, 1.95, "5", lx=5.65, ly=1.5, fs=nfs, color="#2563eb")
    arrow(ax, 4.9, 1.85, 6.4, 0.7, "6", lx=5.15, ly=0.95, fs=nfs, rad=0.25)
    arrow(ax, 6.4, 0.45, 4.9, 1.6, "7", lx=5.7, ly=0.5, fs=nfs, rad=0.25, color="#16a34a")
    arrow(ax, 2.8, 1.9, 2.1, 1.9, "8", lx=2.45, ly=1.5, fs=nfs, color="#16a34a")
    items = [(0.1, 3.9, "3", "R  (referral to the .com TLD server)"),
             (0.1, 3.0, "5", "R  (referral to foo.com's authoritative server)"),
             (0.1, 0.85, "7", "A  (the answer: www.foo.com is 3.4.5.6)"),
             (0.1, 0.0, "8", "A  (the answer, now cached by the resolver)")]
    for x, y, tag, text in items:
        if solution:
            ax.add_patch(Rectangle((x, y), 4.5, 0.8, fc="#f1f5f9", ec="#64748b", lw=1.0))
            ax.text(x + 0.08, y + 0.4, f"{tag}: {text}", ha="left", va="center", fontsize=8, family=FONT)
        else:
            blank(ax, x, y, 4.5, 0.8, f"message {tag} carries:")
    if solution:
        ax.add_patch(Rectangle((1.95, 1.45), 0.95, 1.35, fc="none", ec="#dc2626", lw=2.0))
        ax.text(2.45, 2.82, "DoH encrypts this hop", ha="center", fontsize=8, family=FONT, color="#dc2626", weight="bold")
    save(fig, "dns-lookup-solution" if solution else "dns-lookup")


# -------------------------------------------------------------- Kaminsky attack
def kaminsky(solution):
    fig, ax = setup(9.5, 5.0)
    box(ax, 0.1, 2.6, 1.8, 0.9, "stub resolver", fc="#ffffff")
    box(ax, 3.2, 2.6, 2.0, 0.9, "local recursive\nresolver", fc="#dbeafe")
    box(ax, 6.8, 3.6, 2.6, 0.9, "authoritative\nfor google.com", fc="#dcfce7")
    box(ax, 6.9, 1.25, 2.5, 0.9, "off-path attacker", fc="#fecaca", ec="#b91c1c", lw=1.8)
    arrow(ax, 1.9, 3.05, 3.2, 3.05, "google.com?", lx=2.55, ly=3.6, fs=8.5)
    arrow(ax, 5.2, 3.3, 6.8, 4.0, "google.com?   txid = 0x3a7f", lx=4.9, ly=4.4, rad=-0.1, fs=8.5)
    arrow(ax, 6.8, 3.85, 5.2, 3.1, "142.250.x.x   (txid 0x3a7f)", lx=7.9, ly=3.1, rad=-0.1,
          color="#16a34a", fs=8.5)
    arrow(ax, 6.9, 1.7, 5.2, 2.75, "", ls="--", color="#b91c1c", lw=2.0, rad=0.1)
    if solution:
        ax.add_patch(Rectangle((1.8, 0.05), 4.8, 2.25, fc="#fff1f2", ec="#b91c1c", lw=1.2))
        ax.text(1.9, 1.9, "google.com = 6.6.6.6", ha="left", va="center", fontsize=8, family=FONT, color="#b91c1c", weight="bold")
        ax.text(1.9, 1.4, "one forged reply for EVERY txid", ha="left", va="center", fontsize=7.5, family=FONT, color="#b91c1c")
        ax.text(1.9, 0.9, "0x0000 … 0xffff (65,536 of them)", ha="left", va="center", fontsize=7.5, family=FONT, color="#b91c1c")
    else:
        blank(ax, 1.8, 0.05, 4.8, 2.25, "what the attacker sends:")
    ax.text(4.75, 4.8, "The recursive resolver's cache entry for google.com has just expired", ha="center", fontsize=8.5,
            family=FONT, weight="bold")
    save(fig, "kaminsky-solution" if solution else "kaminsky")


for s in (False, True):
    oauth(s); dns(s); kaminsky(s)
print("done")

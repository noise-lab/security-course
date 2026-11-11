"""Figures for 11-PrivacyLaw: consent defaults (Johnson & Goldstein 2003) and the US statute timeline.

Run from docs/slides: python3 src/privacy_law_figures.py  -> 11-PrivacyLaw/images/*.svg
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "11-PrivacyLaw/images/"
plt.rcParams.update({"font.family": "Helvetica", "font.size": 15, "svg.fonttype": "none"})

# 1. Effective consent rates for organ donation by default (Johnson & Goldstein, Science 2003)
optin = [("Denmark", 4.25), ("Netherlands", 27.5), ("United Kingdom", 17.17), ("Germany", 12.0)]
optout = [("Austria", 99.98), ("Belgium", 98.0), ("France", 99.91), ("Hungary", 99.97),
          ("Poland", 99.5), ("Portugal", 99.64), ("Sweden", 85.9)]
fig, ax = plt.subplots(figsize=(9.5, 4.6))
names = [n for n, _ in optin] + [n for n, _ in optout]
vals = [v for _, v in optin] + [v for _, v in optout]
colors = ["#c0504d"] * len(optin) + ["#4f81bd"] * len(optout)
bars = ax.bar(range(len(vals)), vals, color=colors, width=0.7)
ax.set_xticks(range(len(vals)))
ax.set_xticklabels(names, rotation=30, ha="right")
ax.set_ylabel("Share consenting (%)")
ax.set_ylim(0, 122)
ax.axvline(len(optin) - 0.5, color="#888", ls="--", lw=1)
ax.text(1.5, 108, "Opt-in default\n(must say yes)", ha="center", color="#c0504d", fontsize=14, weight="bold")
ax.text(len(optin) + 3, 110, "Opt-out default\n(must say no)", ha="center", color="#4f81bd", fontsize=14, weight="bold")
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 1.5, f"{v:.0f}", ha="center", fontsize=12)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(OUT + "consent-defaults.svg")

# 2. US privacy statutes by year, labelled with the trigger
events = [
    (1970, "FCRA", "credit bureaus"),
    (1974, "Privacy Act\nFERPA", "federal agencies;\nschools"),
    (1988, "VPPA", "Bork's video\nrentals leaked"),
    (1994, "DPPA", "states selling\nDMV data"),
    (1996, "HIPAA", "health records\nportability"),
    (1998, "COPPA", "children\nunder 13"),
    (1999, "GLBA", "banks sharing\nwith affiliates"),
    (2003, "CA breach\nnotification", "first breach\nnotice law"),
    (2008, "GINA", "genetic\ndiscrimination"),
    (2018, "CCPA", "first state\nomnibus law"),
    (2026, "~20 state\nlaws", "no federal\nomnibus law"),
]
fig, ax = plt.subplots(figsize=(14, 5.8))
ax.hlines(0, 1966, 2030, color="#444", lw=2)
for i, (y, name, why) in enumerate(events):
    tier = [1.0, -1.0, 3.4, -3.4][i % 4]
    up = tier > 0
    ax.plot([y], [0], "o", color="#800000", ms=9, zorder=3)
    ax.vlines(y, 0, tier, color="#999", lw=1)
    ax.text(y, tier + (0.1 if up else -0.1), f"{name}\n{y}", ha="center", va="bottom" if up else "top",
            fontsize=13, weight="bold")
    ax.text(y, tier + (1.55 if up else -1.55), why, ha="center", va="bottom" if up else "top", fontsize=11.5, color="#444")
ax.set_xlim(1966, 2031)
ax.set_ylim(-6.4, 6.4)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUT + "statute-timeline.svg")
print("ok")

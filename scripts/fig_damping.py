"""Figure 2: real-time and batch work cost of amplitude damping.

Real time:  T_rt(p) = max_{0<=y<=p} [h(y) - a y]                       (Theorem 2b)
Batch:      T(p)    = max_{0<=x<=1} [h(x) - h((1-p)x) - a p x]          (Faist-Berta-Brandao capacity)
with a = beta*Delta/ln 2, in bits (units of k_B T ln 2 per use).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "serif", "font.serif": ["DejaVu Serif"], "mathtext.fontset": "cm"})

def h(x):
    x = np.clip(x, 1e-300, 1.0)
    y = np.clip(1.0 - x, 1e-300, 1.0)
    return -(x * np.log2(x) + y * np.log2(y)) * ((x > 0) & (x < 1))

grid = np.linspace(0.0, 1.0, 20001)

def t_rt(p, a):
    y = grid * p
    return np.max(h(y) - a * y)

def t_batch(p, a):
    x = grid
    return np.max(h(x) - h((1.0 - p) * x) - a * p * x)

if __name__ == "__main__":
    ps = np.linspace(0.0, 1.0, 401)
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    for bd, col in [(0.0, "C0"), (1.0, "C1"), (3.0, "C2")]:
        a = bd / np.log(2)
        rt = np.array([t_rt(p, a) for p in ps])
        bt = np.array([t_batch(p, a) for p in ps])
        assert np.all(rt >= bt - 1e-9)
        assert abs(rt[-1] - bt[-1]) < 1e-6          # full reset: no surcharge
        lab = r"$\beta\Delta=%g$" % bd
        ax.plot(ps, rt, color=col, lw=1.8, label=lab)
        ax.plot(ps, bt, color=col, lw=1.4, ls="--")
    ax.set_xlabel(r"damping probability $p$")
    ax.set_ylabel(r"work per use (units of $k_{\mathrm{B}}T\ln 2$)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.22)
    ax.legend(fontsize=7.5, frameon=False, ncol=3, loc="upper center",
              handlelength=1.6, columnspacing=1.2)
    fig.tight_layout()
    fig.savefig("paper/fig-damping.pdf")
    for bd in (0.0, 1.0, 3.0):
        a = bd / np.log(2)
        print("betaDelta=%g  p=0.5: real time %.4f, batch %.4f;  p=1: %.4f vs %.4f"
              % (bd, t_rt(0.5, a), t_batch(0.5, a), t_rt(1, a), t_batch(1, a)))

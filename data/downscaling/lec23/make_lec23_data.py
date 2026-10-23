"""Generates the SYNTHETIC data of Lecture 23 (spatial downscaling): fine_obs.csv and fine_target.csv.
Run from anywhere:  python make_lec23_data.py   (writes the CSVs next to this script).
Nothing here is real data. Replace the arrays by gridded rainfall (e.g. IMD) for real work."""
import numpy as np
from pathlib import Path
from scipy.stats import gamma, norm

out = Path(__file__).parent
rng = np.random.default_rng(23)
H, T = 30, 5                                   # 30 observed years, 5 target years

# fine climatology mu_x (mm/day) on a 4 x 4 grid; row 0 is the southern row, column 0 the western column
mu_x = np.array([[1.6, 3.4, 4.2, 3.8],
                 [1.9, 3.1, 3.6, 4.4],
                 [2.4, 3.8, 2.1, 2.5],
                 [2.2, 3.6, 1.9, 3.5]]).ravel()

# spatially correlated normal scores (correlation decays with distance), then gamma marginals with shape 3
rr, cc = np.divmod(np.arange(16), 4)
d = np.hypot(rr[:, None] - rr[None, :], cc[:, None] - cc[None, :])
rho = 0.55 + 0.45 * np.exp(-d / 1.5)
Z = rng.multivariate_normal(np.zeros(16), rho, size=H + T)
X = gamma.ppf(norm.cdf(Z), a=3.0, scale=mu_x / 3.0)

np.savetxt(out / "fine_obs.csv", X[:H], delimiter=",", fmt="%.3f")      # H x p, the observed period
np.savetxt(out / "fine_target.csv", X[H:], delimiter=",", fmt="%.3f")   # T x p, the "truth" of the target years
print("written to", out)

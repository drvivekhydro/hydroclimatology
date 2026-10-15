"""Generates the SYNTHETIC input files of Lecture 23 (spatial downscaling).
Run from anywhere:  python make_lec23_data.py   (writes the CSVs next to this script).
Nothing here is real data. Swap in IMD gridded rainfall (fine) and a CMIP6 field (coarse) for real work."""
import numpy as np
from pathlib import Path
from scipy.ndimage import zoom

out = Path(__file__).parent
rng = np.random.default_rng(23)
NF, NC, F = 16, 4, 4                      # fine grid 16x16, coarse grid 4x4, factor 4

# ---- terrain: a N-S windward ridge near column 5 plus a smaller hill (clearly synthetic)
yy, xx = np.mgrid[0:NF, 0:NF]
ridge = np.exp(-((xx - (5 + 0.15 * (yy - 8))) / 1.6) ** 2)
hill = 0.5 * np.exp(-((xx - 11) ** 2 + (yy - 4) ** 2) / (2 * 1.5 ** 2))
elev = 1.6 * (ridge + hill) / (ridge + hill).max()          # km
shape = elev / elev.max()                                    # 0..1 terrain index

def block_mean(a):                                           # (..., 16, 16) -> (..., 4, 4)
    s = a.shape[:-2]
    return a.reshape(*s, NC, F, NC, F).mean(axis=(-3, -1))

def make_days(n):
    g = rng.standard_normal(n)                               # domain-wide wetness of the day
    u = 0.7 * g + 0.7 * rng.standard_normal(n)               # strength of onshore flow
    amp = np.exp(0.5 * u - 0.125)                            # orographic enhancement of the day
    smooth = np.array([zoom(rng.standard_normal((5, 5)), NF / 5, order=3) for _ in range(n)])
    smooth /= smooth.std()
    Z = 0.6 * g[:, None, None] + 0.8 * smooth + 0.15 * rng.standard_normal((n, NF, NF))
    base = 3.0                                               # mm/day
    R = base * (1 + 4.0 * amp[:, None, None] * shape) * np.exp(0.55 * Z - 0.55 ** 2 / 2)
    return R

def make_gcm(fine):
    C = block_mean(fine)
    a = np.array([[1.5, 1.3, 1.1, 0.9], [1.4, 1.2, 1.0, 0.8],
                  [1.3, 1.1, 0.9, 0.8], [1.2, 1.0, 0.9, 0.7]])   # wet west, dry east
    eps = rng.standard_normal(C.shape)
    return a * (C * np.exp(0.12 * eps)) ** 1.15

train, test = make_days(240), make_days(60)
gtr, gte = make_gcm(train), make_gcm(test)

def save(name, arr, fmt="%.3f"):
    np.savetxt(out / name, arr, delimiter=",", fmt=fmt)

save("terrain_elevation_km_16x16.csv", elev, "%.4f")
save("fine_obs_train.csv", train.reshape(len(train), -1))
save("fine_obs_test.csv", test.reshape(len(test), -1))
save("gcm_coarse_train.csv", gtr.reshape(len(gtr), -1))
save("gcm_coarse_test.csv", gte.reshape(len(gte), -1))

# ---------------- tiny worked examples (identical numbers in the spreadsheet) ----------------
save("bilinear_coarse_4x4.csv", np.array([[12, 18, 10, 6], [20, 30, 16, 9], [14, 22, 13, 7], [8, 11, 9, 5]]), "%g")
save("bilinear_points_xy.csv", np.array([[0.5, 0.5], [1.25, 1.75], [1.0, 1.0], [2.4, 0.6], [0.2, 2.8], [2.9, 2.9]]), "%g")
save("bcsd_coarse_clim_2x2.csv", np.array([[2.0, 4.0], [6.0, 8.0]]), "%g")
save("bcsd_gcm_bc_today_2x2.csv", np.array([[3.0, 4.0], [3.0, 12.0]]), "%g")
save("bcsd_fine_clim_4x4.csv", np.array([[1.0, 3.0, 3.0, 5.0], [1.5, 2.5, 3.5, 4.5], [4.0, 8.0, 6.0, 10.0], [5.0, 7.0, 7.0, 9.0]]), "%g")
save("bcsd_T_coarse_clim_2x2.csv", np.array([[24.0, 22.0], [20.0, 18.0]]), "%g")
save("bcsd_T_gcm_bc_today_2x2.csv", np.array([[26.0, 23.0], [21.0, 17.0]]), "%g")
save("bcsd_T_fine_clim_4x4.csv", np.array([[25.5, 22.5, 22.5, 21.5], [25.0, 23.0, 22.5, 21.5],
                                           [21.0, 20.0, 18.5, 17.5], [20.0, 19.0, 18.5, 17.5]]), "%g")
# constructed-analogue tiny library: 8 days of a 4x4 fine field (row-major, 16 values)
rl = np.random.default_rng(5)
b4 = np.array([[1.0, 3.0, 3.0, 5.0], [1.5, 2.5, 3.5, 4.5], [4.0, 8.0, 6.0, 10.0], [5.0, 7.0, 7.0, 9.0]])
lib = []
for d in range(8):
    amp = rl.uniform(0.6, 1.8)
    pat = b4 * amp * np.exp(0.3 * rl.standard_normal((4, 4)))
    lib.append(np.round(pat.ravel(), 1))
lib = np.array(lib)
truth = np.round((b4 * 1.4 * np.exp(0.3 * rl.standard_normal((4, 4)))).ravel(), 1)
tgt = np.round(truth.reshape(2, 2, 2, 2).mean(axis=(1, 3)).ravel() * np.array([1.05, 0.95, 1.0, 1.05]), 1)
save("ca_library_fine_8x16.csv", lib, "%g")
save("ca_target_coarse_1x4.csv", tgt.reshape(1, 4), "%g")
save("ca_target_truth_fine_1x16.csv", truth.reshape(1, 16), "%g")
print("written to", out)

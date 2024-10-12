import numpy as np
import scipy.stats as st
from scipy.special import gamma

_D_TABLE = {
    2: {
        "d2": 0.7,
        "d3": 0.8,
    },
}


def d(m: int, sim_size: int = 100_000) -> float:
    if m < 2:
        raise ValueError("Sample size m has to be >= 2.")

    if m in _D_TABLE:
        return _D_TABLE[m]["d2"], _D_TABLE[m]["d3"]

    x = st.norm.rvs(size=(sim_size, m))
    R_i = x.max(axis=1) - x.min(axis=1)
    d2 = np.mean(R_i)
    d3 = np.std(R_i, ddof=1)
    return d2, d3


def c4(m: int) -> float:
    return gamma(m / 2) / gamma((m - 1) / 2) * np.sqrt(2 / (m - 1))


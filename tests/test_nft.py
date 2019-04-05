from __future__ import division
import numpy as np
import scipy.optimize as opt
from nftopt import nakanishi_fujii_todo
import pytest


def test_nakanishi_fujii_todo():

    param = np.linspace(0, 2 * np.pi, 100)
    fun = lambda x: np.sum(np.cos(x))

    res = opt.minimize(
        fun,
        param,
        options={'maxfev': 200, 'reset_interval': -1},
        method=nakanishi_fujii_todo,
        callback=fun
    )
    print(res.x % (2 * np.pi))
    assert np.allclose(np.ones_like(param) * np.pi, res.x % (2 * np.pi))

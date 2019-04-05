from __future__ import division
import numpy as np
from scipy.optimize import OptimizeResult


def nakanishi_fujii_todo(fun, x0, args=(), maxfev=1024, reset_interval=32, eps=1e-32, callback=None, **_):
    """
    Find the global minimum of a function using the nakanishi_fujii_todo
    algorithm [1].
    Parameters
    ----------
    fun : callable ``f(x, *args)``
        Function to be optimized.  ``args`` can be passed as an optional item
        in the dict ``minimizer_kwargs``.
        This function must satisfy the three condition written in Ref. [1].
    x0 : ndarray, shape (n,)
        Initial guess. Array of real elements of size (n,),
        where 'n' is the number of independent variables.
    args : tuple, optional
        Extra arguments passed to the objective function.
    maxfev : int
        Maximum number of function evaluations to perform.
        Default: 1024.
    reset_interval : int
        The minimum estimates directly once in ``reset_interval`` times.
        Default: 32.
    callback : callable, optional
        Called after each iteration.
    Returns
    -------
    res : OptimizeResult
        The optimization result represented as a ``OptimizeResult`` object.
        Important attributes are: ``x`` the solution array. See
        `OptimizeResult` for a description of other attributes.
    Notes
    -----
    In this optimization method, the optimization function have to satisfy
    three conditions written in [1].
    References
    ----------
    .. [1] K. M. Nakanishi, K. Fujii, and S. Todo. 2019.
        Sequential minimal optimization for quantum-classical hybrid algorithms.
        arXiv preprint arXiv:1903.12166.
    Examples
    --------
    >>> from scipy.optimize import minimize
    >>> from nftopt import nakanishi_fujii_todo


    >>> res = minimize(
    >>>     YOUR_FUNC,
    >>>     YOUR_PARAM,
    >>>     options={'maxfev': 2048},
    >>>     method=nakanishi_fujii_todo,
    >>>     callback=YOUR_EVAL_FUNC
    >>> )
    """

    x0 = np.asarray(x0)
    recycle_z0 = None
    niter = 0
    funcalls = 0

    while True:

        idx = niter % x0.size

        if reset_interval > 0:
            if niter % reset_interval == 0:
                recycle_z0 = None

        if recycle_z0 is None:
            z0 = fun(np.copy(x0), *args)
            funcalls += 1
        else:
            z0 = recycle_z0

        p = np.copy(x0)
        p[idx] = x0[idx] + np.pi / 2
        z1 = fun(p, *args)
        funcalls += 1

        p = np.copy(x0)
        p[idx] = x0[idx] - np.pi / 2
        z3 = fun(p, *args)
        funcalls += 1

        z2 = z1 + z3 - z0
        c = (z1 + z3) / 2
        a = np.sqrt((z0 - z2) ** 2 + (z1 - z3) ** 2) / 2
        b = np.arctan((z1 - z3) / ((z0 - z2) + 1e-32 * (z0 == z2))) + x0[idx]
        b += 0.5 * np.pi + 0.5 * np.pi * np.sign((z0 - z2) + eps * (z0 == z2))

        x0[idx] = b
        recycle_z0 = c - a

        if callback is not None:
            callback(np.copy(x0))

        if funcalls >= maxfev:
            break

        niter += 1

    return OptimizeResult(fun=fun(np.copy(x0)), x=x0, nit=niter, nfev=funcalls, success=(niter > 1))

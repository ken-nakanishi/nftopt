# Nakanishi-Fujii-Todo method for scipy.optimize

This is Nakanishi-Fujii-Todo method (arXiv:1903.12166) for `scipy.optimize.minimize`.

The optimization function have to satisfy three conditions written in [1].

## install 

```sh
pip install nftopt
```
or
```sh
pip3 install nftopt
```

## Example code
```python
from scipy.optimize import minimize
from nftopt import nakanishi_fujii_todo


res = minimize(
    YOUR_FUNC,
    YOUR_PARAM,
    options={'maxfev': 2048},
    method=nakanishi_fujii_todo,
    callback=YOUR_EVAL_FUNC
)
```

## Reference
[1] K. M. Nakanishi, K. Fujii, and S. Todo. 2019.
Sequential minimal optimization for quantum-classical hybrid algorithms.
arXiv preprint arXiv:1903.12166.
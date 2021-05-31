import math
import numpy as np

def float_rate_bond(maturity, coupon_freq, amount, mu1, sigma1,mu2, sigma2, n_reps,r0,v0)
'''
in case of float rate bond, there are two prediction mechanism. We should forecast projection and discount curves, and 
also we can use Jarrow-Yidilrim Framework for arbitrage-free forward rate drift restrictions on nominal rate and real rate
'''
    delta_t = 0.001
    payoff_sum = 0
    for j in range(num_reps):
        rt = r0
        vt = v0
        rt = rt * math.exp((mu1 - 0.5 * sigma1 ** 2) * delta_t + sigma * np.sqrt(delta_t) * np.random.normal(0, 1))
        vt = vt * math.exp((mu2 - 0.5 * sigma2 ** 2) * delta_t + sigma * np.sqrt(delta_r) * np.random.normal(0, 1))
        payoff = amount * rt^j/(1+vt)^j
        payoff_sum += payoff

    return payoff_sum
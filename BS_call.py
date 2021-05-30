import numpy as np
from scipy.stats import norm


def black_scholes_call_risk_free(S0, strike, q, maturity, r, sigma):
    """
    :param S0: current price
    :param strike: strike price
    :param q: dividends yield
    :param maturity: maturity in working days
    :param r: risk - free rate
    :param sigma: volatiliry
    :return: Option price with Black-Sholes model
    """
    d1 = (np.log(S0 / strike) + (r - q + sigma ** 2 / 2) * maturity) / sigma * np.sqrt(maturity)
    d2 = d1 - sigma * np.sqrt(maturity)

    call = S0 * np.exp(-q * maturity) * norm.cdf(d1) - strike * np.exp(-r * maturity) * norm.cdf(d2)
    return call

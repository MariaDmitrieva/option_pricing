import numpy as np
import math


def mc_euro_options(option_type, aux, s0, strike, maturity, r, sigma, num_reps):
    payoff_sum = 0
    for j in range(num_reps):
        st = s0
        st = st * math.exp((r - 0.5 * sigma ** 2) * maturity + sigma * np.sqrt(maturity) * np.random.normal(0, 1))
        if option_type == 'c':
            if aux:
                payoff = max(0, st - strike)
            else:
                payoff = min(0, st - strike)
        elif option_type == 'p':
            if aux:
                payoff = max(0, strike - st)
            else:
                payoff = min(0, strike - st)
        payoff_sum += payoff
    premium = (payoff_sum / float(num_reps)) * math.exp(1) ** (-r * maturity)
    return premium

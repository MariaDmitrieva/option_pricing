import numpy as np
import math
import classic_option


def compound_euro_options(option_type, aux, S0, strike, strike_compound, maturity, maturity_compound, mu, sigma,
                          num_reps):
    """

    :param option_type: Type of  option (Call or Put)
    :param aux: Type of payoff
    :param S0: current price of underlying
    :param strike: strike price of option underlying
    :param strike_compound: strike of compound option
    :param maturity: matyrity date of base option
    :param maturity_compound: matyrity of compound option
    :param mu: mean of underlying
    :param sigma: volatility
    :param num_reps: N of iteration
    :return: price of compound option
    """
    payoff_sum = 0
    for j in range(num_reps):
        vt = classic_option.euro_options_risk_free(option_type, aux, S0, strike, maturity, mu, sigma, num_reps)
        vt = vt * math.exp(
            (mu - 0.5 * sigma ** 2) * maturity_compound + sigma * np.sqrt(maturity_compound) * np.random.normal(0, 1))

        if option_type == 'c':
            if aux:
                payoff = max(0, vt - strike_compound)
            else:
                payoff = min(0, vt - strike_compound)
        elif option_type == 'p':
            if aux:
                payoff = max(0, strike - vt)
            else:
                payoff = min(0, strike - vt)
        payoff_sum += payoff
    premium = (payoff_sum / float(num_reps)) * math.exp(1) ** (-mu * maturity_compound)
    return premium

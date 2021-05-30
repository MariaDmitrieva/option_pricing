import classic_option as cl

# option_type, aux, s0, strike, maturity, r, sigma, num_reps
print(cl.mc_euro_options('c', True, 927.96, 785, 100.0 / 252, 0.01, 0.23, 500))
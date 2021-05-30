import classic_option as cl
import classic_option_without_rf as cl1
import BS_call as bs

print(cl.euro_options_risk_free('c',True,100,110,100/252,0.05,0.25,1000))
print(cl1.euro_options('c',True,100,110,100/252,0.1,0.25,1000))
print(bs.black_scholes_call_risk_free(100,110,0,100/252,0.05,0.25))
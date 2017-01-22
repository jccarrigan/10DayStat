import math

def cumul(mu, std, x):
    erf = math.erf((x-mu)/(std*math.sqrt(2)))
    return 0.5*(1+erf)

print round(cumul(100*2.4, 10*2.0, 250), 4)

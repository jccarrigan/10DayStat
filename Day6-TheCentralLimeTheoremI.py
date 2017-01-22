import math

def cumul(mu, std, x):
    erf = math.erf((x-mu)/(std*math.sqrt(2)))
    return 0.5*(1+erf)

print round(cumul(205*49, 7*15, 9800), 4)

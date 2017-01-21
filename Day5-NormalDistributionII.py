import math
                     
def cumul(mu, std, x):
    erf = math.erf((x-mu)/(std*math.sqrt(2)))
    return 0.5*(1+erf)

print round(cumul(20.0, 2.0, 19.5), 3)
print round(cumul(20.0, 2.0, 22)-cumul(20, 2, 20), 3)

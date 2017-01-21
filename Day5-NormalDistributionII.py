import math
                     
def cumul(mu, std, x):
    erf = math.erf((x-mu)/(std*math.sqrt(2)))
    return 0.5*(1+erf)

print round((1-cumul(70.0, 10.0, 80.0))*100, 2)
print round((1-cumul(70.0, 10.0, 60))*100, 2)
print round(cumul(70.0, 10.0, 60)*100, 2)

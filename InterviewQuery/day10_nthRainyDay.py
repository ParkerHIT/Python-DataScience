

#rY AND rT --> 20% rTom

#rY OR rT --> 60% rTom

#nrY AND nrT --> 20% rTom

#n = 1

#20% rTom -- > 20% rDaT
#80% nrTom --> 60% rDaT

import numpy as np
from numpy.linalg import matrix_power

def rain_days(n):
    P = np.zeros((4,4))
    P[0,0] = 0.2
    P[0,1] = 0.8
    P[1,2] = 0.6
    P[1,3] = 0.4
    P[2,0] = 0.6
    P[2,1] = 0.4
    P[3,2] = 0.2
    P[3,3] = 0.8
    P = matrix_power(P,n)
    prob = P[0,0] + P[0,2]
    return prob

if __name__ == "__main__":
    day = input("Enter Days:")
    p_day = rain_days(int(day))
    print("Probablity of rain on day", day, " after today is" , p_day)




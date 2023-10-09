
#Greatest Common Denominator
#https://www.interviewquery.com/questions/greatest-common-denominator

import math

def gcd(numbers):
    
    gcd = numbers[0]
    for i in range(1, len(numbers)):
        gcd = math.gcd(gcd, numbers[i])
    return gcd 
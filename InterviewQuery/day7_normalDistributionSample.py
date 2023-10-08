#https://www.interviewquery.com/questions/normal-distribution-sample
#Write a function to get a sample from a standard normal distribution.


import numpy as np

def normal_distribution_sample():
    #Standard Norm Dist with mean = 0, SD =1 
    return np.random.normal(0, 1)
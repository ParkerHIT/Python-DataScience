
#https://www.interviewquery.com/questions/nightly-job

import numpy as np
import random 

def simulate_overlap():
    task1 = np.random.randint(0, 300, size = 10000)
    task2 = np.random.randint(0, 300, size = 10000)
    
    overlap_percentage = np.mean(np.abs(task1 - task2) <= 60)
    annual_cost = overlap_percentage * 365 * 1000
    return annual_cost


    

#1873. Calculate Special Bonus

#https://leetcode.com/problems/calculate-special-bonus/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    
    df = employees
    for index, row in df.iterrows():
        if row['name'].startswith('M') or row['employee_id'] % 2 == 0:
            df.loc[index, 'salary'] = 0
    df = df.rename(columns={'salary': 'bonus'})
    df.drop(columns=['name'], inplace=True)
    df = df.sort_values(by = 'employee_id')
    #print(df)
    return df
    
    
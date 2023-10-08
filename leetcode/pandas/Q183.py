#183. Customers Who Never Order

#https://leetcode.com/problems/customers-who-never-order/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_customers(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:

    merged_df = pd.merge(df1, df2, left_on='id', right_on='customerId', how='left', indicator=True)
    filtered_df = merged_df[merged_df['_merge'] == 'left_only'].drop('_merge', axis=1)
    filtered_df = filtered_df.rename(columns={'name': 'Customers'})
    filtered_df.drop(columns=['id_x','id_y','customerId'], inplace=True)
    print(filtered_df)

    
    return filtered_df
    
    
if __name__ == "__main__":
    
    data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
    customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
    data = [[1, 3], [2, 1]]
    orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})
    df = find_customers(customers,orders)
    
    print(df.to_string(index=False))

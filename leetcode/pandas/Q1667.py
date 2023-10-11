
# 1667. Fix Names in a Table

# https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = users
    df['name'] = df['name'].str.capitalize()
    sorted_df = df.sort_values(by='user_id')
    return sorted_df
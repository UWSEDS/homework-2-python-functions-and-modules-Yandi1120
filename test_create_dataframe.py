# Question 1
import pandas as pd
data = pd.read_csv('https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD')

# Question 2
import numpy as np

def same_type(data_list):
    is_same_type = True
    first_item = data_list[0]
    for item in data_list[1:]:
        if type(first_item) == type(item) or np.isnan(item):
            pass
        else:
             is_same_type = False
    return is_same_type

def test_create_dataframe(pd_df, col_list):
    result = True
    df_col_list = pd_df.columns.tolist()
    if pd_df[df_col_list[0]].count() + 1 >= 10:
        if len(pd_df.columns) == len(col_list):
            for col in col_list:
                if col in df_col_list:
                    if same_type(pd_df[col]):
                        pass
                    else: result = False
                else:
                    result = False  
        else:
            result = False
    else:
        result = False
    return result

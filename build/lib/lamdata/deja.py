import numpy as np
import pandas as pd
print("Hi Github Users!")

def obj_lister(df):
    """
    This function take in a dataframe and returns a list of columns that contain objects
    """
    obj_list = []
    for col in df.select_dtypes([np.object]):
        obj_list.append(col)
    return obj_list

def NaN_cleaning(df):
    """
    This function thakes in a dataframe and cleans nulls by replacing with text. It returns a
    cleaned dataframe.
    """
    df = df.replace(np.nan, 'unknown')
    return df.reset_index(drop=True)
print('Installed!')
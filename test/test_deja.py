import unittest
import numpy as np
import pandas as pd
from lamdata.deja import obj_lister, NaN_cleaning
                
class TestDataFrame(unittest.TestCase):
    def test_NaN_cleaning(self):
        DATA_PATH = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-2-Kaggle-Challenge/master/data/'
        train = pd.merge(pd.read_csv(DATA_PATH+'waterpumps/train_features.csv'), 
                 pd.read_csv(DATA_PATH+'waterpumps/train_labels.csv'))
        train = NaN_cleaning(train)
        self.assertEqual(len(list(train.columns)), 41)
        self.assertEqual(train["funder"][0], "Roman")
if __name__ == "__main__":
    unittest.main()

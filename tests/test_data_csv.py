import pandas as pd

import sys
import os
sys.path.append(os.getcwd())
print('hello')
print(os.getcwd())

from src.data_csv import data


def test_duplicate():
    assert not data.duplicated().any()
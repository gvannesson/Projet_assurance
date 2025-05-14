import pandas as pd

import sys
import os
sys.path.append(os.getcwd())
from src.data_csv import drop_dup
from io import StringIO
from csv import reader



mon_mock=StringIO(
    "age,sex,bmi,children,smoker,region,charges\n"
    "19,female,27.9,0,yes,southwest,16884.924\n"
    "18,male,33.77,1,no,southeast,1725.5523\n"
    "28,male,33,3,no,southeast,4449.462\n"
    "33,male,22.705,0,no,northwest,21984.47061\n"
    "18,male,33.77,1,no,southeast,1725.5523\n"
)

mock_csv=pd.read_csv(mon_mock)

drop_dup(mock_csv)

def test_duplicate():
    assert not mock_csv.duplicated().any()
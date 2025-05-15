import pandas as pd
import os

def readcsv(csv):
    data = pd.read_csv(csv)
    return data

def drop_dup(data):
    data.drop_duplicates(inplace=True, ignore_index=True)
    return data


if os.path.isfile('dataset.csv'):
    drop_dup(readcsv('dataset.csv'))

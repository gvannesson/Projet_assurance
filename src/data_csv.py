import pandas as pd

data = pd.read_csv('dataset.csv')

def drop_dup(data):
    data.drop_duplicates(inplace=True, ignore_index=True)
    return data


drop_dup(data)
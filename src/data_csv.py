import pandas as pd


def readcsv(csv):
    data = pd.read_csv(csv)
    return data

def drop_dup(data):
    data.drop_duplicates(inplace=True, ignore_index=True)
    return data


drop_dup(readcsv('dataset.csv'))
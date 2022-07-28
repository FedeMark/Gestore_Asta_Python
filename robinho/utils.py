import pandas as pd


def get_series_value(series: pd.Series, index):
    if index in series.index:
        return series[index]

    return 0

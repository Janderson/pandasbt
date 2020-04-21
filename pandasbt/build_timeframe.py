import pandas as pd
import numpy as np

def build_timeframe(dataframe, timeframe="D1", datetime_column="time", filter_at_end=True):
    """ 
        function: build_timeframe
        This function should build a highertimeframe like D1, using a lower timeframe like M1
    """
    dataframe["time"] = pd.to_datetime(dataframe["time"])
    dataframe.sort_values(["time"], ascending=True, inplace=True)
    
    dataframe["start_bar_sign"] = dataframe.time.dt.day !=  dataframe.time.dt.day.shift(1)
    dataframe["close_bar_sign"] = (dataframe.start_bar_sign.shift(-1)) | (dataframe.index == dataframe.index[-1])

    dataframe["open_bar"] = np.where(dataframe.start_bar_sign, dataframe.open, np.nan)
    dataframe["close_bar"] = np.where(dataframe.close_bar_sign, dataframe.close, np.nan)
    dataframe["low_bar"] = dataframe.groupby((dataframe.start_bar_sign).cumsum()).low.cummin()
    dataframe["high_bar"] = dataframe.groupby((dataframe.start_bar_sign).cumsum()).high.cummax()
    
    dataframe.fillna(method="ffill", inplace=True)
    if filter_at_end:
        return dataframe.query("close_bar_sign == True")
    return dataframe
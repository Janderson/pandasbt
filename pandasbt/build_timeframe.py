import pandas as pd
import numpy as np


def build_timeframe(dataframe,
                    timeframe="D1",
                    datetime_column="time",
                    filter_at_end=True):
    """
        function: build_timeframe
        This function should build a highertimeframe like D1,
        using a lower timeframe like M1
    """
    dataframe["time"] = pd.to_datetime(dataframe["time"])
    dataframe.sort_values(["time"], ascending=True, inplace=True)

    if timeframe=="D1":
        dataframe["start_bar_sign"] = dataframe.time.dt.day != dataframe.time.dt.day.shift(1)
        dataframe["close_bar_sign"] = (dataframe.start_bar_sign.shift(-1)) | \
                                    (dataframe.index == dataframe.index[-1])
        dataframe["time_bar"] = dataframe.time.dt.date
    elif timeframe in ["M2", "M5", "M10", "M15", "M20", "M30"]:
        minute = dataframe.time.dt.minute
        hour = dataframe.time.dt.hour
        timeframe_minutes = int(timeframe.upper().replace("M", ""))
        dataframe["number_bar"] = minute - np.mod(minute, timeframe_minutes) + (60*hour)
        dataframe["start_bar_sign"] = dataframe.number_bar != dataframe.number_bar.shift(1)
        dataframe["close_bar_sign"] = (dataframe.start_bar_sign.shift(-1)) | \
                                    (dataframe.index == dataframe.index[-1])
        dataframe["time_bar"] = dataframe.time - pd.TimedeltaIndex(dataframe.time.dt.minute, unit="m") - pd.TimedeltaIndex(dataframe.time.dt.second, unit="s") + pd.TimedeltaIndex(minute - np.mod(minute, timeframe_minutes), unit="m")
    else:
        return Exception("Timeframe {} not implemented".format(timeframe))

    dataframe["open_bar"] = np.where(dataframe.start_bar_sign,
                                     dataframe.open, np.nan)
    dataframe["close_bar"] = np.where(dataframe.close_bar_sign,
                                      dataframe.close, np.nan)
    dataframe["low_bar"] = dataframe.groupby(
                                    (dataframe.start_bar_sign).cumsum()
                           ).low.cummin()
    dataframe["high_bar"] = dataframe.groupby(
                                    (dataframe.start_bar_sign).cumsum()
                           ).high.cummax()

    dataframe.fillna(method="ffill", inplace=True)
    if filter_at_end:
        return dataframe.query("close_bar_sign == True")[["time_bar", "open_bar", "high_bar", "low_bar", "close_bar"]]
    return dataframe


def end_build_timeframe(dataframe, column="close_bar_sign"):
    return dataframe.query("close_bar_sign == True")

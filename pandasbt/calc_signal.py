from pandas import DataFrame
import numpy as np
"""
    Add a signal column into dataframe
    '0' - means nothing
    '-1' - means sell
    '1' - means buy
"""
BUY_VALUE = 1
SELL_VALUE = -1


def calc_return(dataframe, price_column="close", method="pct_ret"):
    if not isinstance(dataframe, DataFrame):
        raise Exception("Should be pandas.Dataframe")
    dataframe = dataframe.copy()
    if method == "pct_ret":
        dataframe["pbt_rets"] = dataframe[price_column].pct_change()
    return dataframe


def calc_signal(dataframe, buy_query="", sell_query="", price_column=""):
    if not isinstance(dataframe, DataFrame):
        raise Exception("Should be pandas.Dataframe")

    dataframe = dataframe.copy()
    dataframe["pbt_signal"] = 0
    if buy_query != "":
        dataframe.pbt_signal = np.where(
            dataframe.index.isin(dataframe.query(
                buy_query).index), BUY_VALUE, dataframe.pbt_signal
        )
    if sell_query != "":
        dataframe.pbt_signal = np.where(
            dataframe.index.isin(dataframe.query(
                sell_query).index), SELL_VALUE, dataframe.pbt_signal
        )

    if price_column != "":
        dataframe = calc_return(dataframe, price_column)

    return dataframe

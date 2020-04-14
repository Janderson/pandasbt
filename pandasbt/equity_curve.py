from pandas import DataFrame


def equity_curve(dataframe, price_column="close"):
    if not isinstance(dataframe, DataFrame):
        raise Exception("Should be pandas.Dataframe")
    dataframe["pbt_rets"] = dataframe[price_column].pct_change()
    dataframe["pbt_rets"].plot()
    return dataframe

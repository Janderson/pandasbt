from pandas import DataFrame


def zscore(dataframe, period, price_column="close", inplace=False):
    if not isinstance(dataframe, DataFrame):
        raise Exception("Should be pandas.Dataframe")
    dataframe["zscore"] = (
        dataframe[price_column] - dataframe[price_column].rolling(
            window=period).mean()) / dataframe[price_column].rolling(
                window=period).std(ddfo=0)
    return dataframe

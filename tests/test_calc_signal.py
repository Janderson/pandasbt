import sys
import os
import pandas as pd
import pytest

# Avoid error module path
sys.path.insert(0, os.path.abspath(  # noqa: E402 - Avoid flake8 error 402
    os.path.join(os.path.dirname(__file__), '..'))
)

from pandasbt import calc_signal
from pandasbt.calc_signal import calc_return
from pandasbt import zscore


@pytest.fixture
def dataframe_default():
    return pd.DataFrame([
        {"close": 25}, {"close": 15}, {"close": 41}, {"close": 7},
        {"close": 5}, {"close": 115}, {"close": 45}, {"close": 32},
    ])


def test_calc_signal_should_signal_with_zeros_and_ones(dataframe_default):
    df_test = dataframe_default
    df_test = calc_signal(zscore(df_test, period=3),
                          buy_query="zscore > 1",
                          sell_query="zscore <= -0.5")
    assert df_test.pbt_signal.iloc[2] == 1
    assert df_test.pbt_signal.iloc[3] == -1
    assert df_test.pbt_signal.iloc[6] == 0


def test_calc_should_calc_a_return_column(dataframe_default):
    df_test = dataframe_default
    df_test = calc_signal(zscore(df_test, period=3),
                          buy_query="zscore > 1",
                          sell_query="zscore <= -0.5")

    assert calc_return(df_test, "close").pbt_rets.iloc[1] == -0.4
    assert calc_return(df_test, "close").pbt_rets.iloc[5] == 22.0


def test_calc_signal_and_returns_at_once(dataframe_default):
    df_test = dataframe_default
    df_test = calc_signal(zscore(df_test, period=3),
                          buy_query="zscore > 1",
                          sell_query="zscore <= -0.5",
                          price_column="close")

    assert df_test.pbt_rets.iloc[1] == -0.4
    assert df_test.pbt_rets.iloc[5] == 22.0


def test_calc_should_not_modify_original_df(dataframe_default):
    df_test = dataframe_default
    calc_signal(zscore(df_test, period=3),
                buy_query="zscore > 1",
                sell_query="zscore <= -0.5",
                price_column="close")
    assert "pbt_signal" not in list(df_test.columns)

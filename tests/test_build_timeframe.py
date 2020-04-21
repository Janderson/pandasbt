import sys
import os
import pandas as pd
import pytest

# Avoid error module path
sys.path.insert(0, os.path.abspath(  # noqa: E402 - Avoid flake8 error 402
    os.path.join(os.path.dirname(__file__), '..'))
)

from pandasbt.build_timeframe import build_timeframe

@pytest.fixture
def dataframe_m1():
    dataframe = pd.DataFrame([
        {"time": "2020-01-01 10:13:00", "open": 12, "high": 20, "low": 12, "close": 17},
        {"time": "2020-01-01 10:14:00", "open": 17, "high": 25, "low": 17, "close": 20},
        {"time": "2020-01-01 10:12:00", "open": 5, "high": 12, "low": 5, "close": 12},
        {"time": "2020-01-01 10:15:00", "open": 20, "high": 21, "low": 15, "close": 16},
        {"time": "2020-01-02 10:00:00", "open": 20, "high": 21, "low": 15, "close": 16},
        ])
    dataframe["time"] = pd.to_datetime(dataframe["time"])
    #dataframe.set_index("time", inplace=True)
    return dataframe


def test_build_timeframe_d1(dataframe_m1):

    first_bar = build_timeframe(dataframe_m1, timeframe="D1").iloc[0]
    
    #import ipdb; ipdb.set_trace()
    assert first_bar.close_bar == 16
    assert first_bar.high_bar == 25
    assert first_bar.low_bar == 5
    assert first_bar.open_bar == 5
    


    
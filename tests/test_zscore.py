import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(  # noqa: E402 - Avoid flake8 error 402
    os.path.join(os.path.dirname(__file__), '..'))
)
from pandasbt import zscore


def test_calc_zscore():
    df_test = pd.DataFrame([
        {"close": 25}, {"close": 15}, {"close": 45}, {"close": 32}
    ])
    assert round(zscore(df_test, 2).zscore.iloc[-1]*100) == -71

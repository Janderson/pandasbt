import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(  # noqa: E402 - Avoid flake8 error 402
    os.path.join(os.path.dirname(__file__), '..'))
)

from pandasbt import equity_curve as eqt


def test_equity_curve():
    df_test = pd.DataFrame([
        {"close": 25}, {"close": 15}, {"close": 45}, {"close": 32}
    ])
    eqt(df_test)
    assert round(df_test["pbt_rets"].iloc[-1]*100) == -29.0

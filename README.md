# PandasBT
Simples Framework to Backtest Strategies using pandas

#### Installation
----------
```
pip install pandasbt
```


#### Calculation a factor zscore
```python
import pandasbt as pbt

df_test = pd.DataFrame([
    {"close": 25}, {"close": 15}, {"close": 41}, {"close": 7},
    {"close": 5}, {"close": 115}, {"close": 45}, {"close": 32},
])

pbt.zscore(df_test)
```

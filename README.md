# PandasBT
Simples Framework to Backtest Strategies using pandas

## Resume:
* [Installation](#Installation)
* [Calculating a factor using zscore](#calculating-a-factor-using-zscore)
* [Calculating Buy and Sell signals](#calculating-buy-and-sell-signals)
* [Calculate a Higher Timeframe using a Lower Timeframe](#calculate-a-higher-timeframe-like-d1-using-a-lower-timeframe-like-m5)

#### Installation
----------
```
pip install pandasbt
```


#### Calculating a factor zscore
```python
import pandasbt as pbt

df_test = pd.DataFrame([
    {"close": 25}, {"close": 15}, {"close": 41}, {"close": 7},
    {"close": 5}, {"close": 115}, {"close": 45}, {"close": 32},
])

pbt.zscore(df_test, period=20)
```
or you can specify the column
```python
pbt.zscore(df_test, 20, "close")
```


#### Calculating Buy and Sell signals
That mean add a signal column into dataframe.  
0 - means nothing  
-1 - means sell  
1 - means buy  

```python
import pandasbt as pbt

df_test = pd.DataFrame([
    {"close": 25}, {"close": 15}, {"close": 41}, {"close": 7},
    {"close": 5}, {"close": 115}, {"close": 45}, {"close": 32},
])

pbt.calc_signal(df_test, buy_query="close > 20", sell_query="close < 10")
```

### Calculate a Higher Timeframe (Like D1) using a Lower Timeframe (Like M5)
```python
import pandasbt as pbt
pbt.build_timeframe(df_test, timeframe="M5)
```

#%%
import pandas as pd
import numpy as np

stocks = ['A', 'B']
dates = ['2013-07-08', '2013-07-09', '2013-07-10', '2013-07-11']

def basics():
    df = pd.DataFrame([[1,2,3,4,5], 
                  ['a','b','c','d','e'],
                  [6,7,8,9,0]])
    print(df)
    print('values', df.values)
    print('index', df.index)

def index_weights():
    prices = pd.DataFrame([
        [2, 2],
        [5, 6],
        [1, 2],
        [6, 5]
    ], index=dates, columns = stocks)

    volume = pd.DataFrame([
        [100, 340],
        [240, 220],
        [120, 500],
        [10, 100]
    ], index = dates, columns = stocks)
    
    print(prices)
    print(volume)

    market_cap = prices * volume

    print(market_cap)
    print(market_cap.sum())

    index_weights = market_cap / market_cap.sum()
    print(index_weights)

def dividends_weights():    
    dividends = pd.DataFrame([
        [0, 0],
        [0, 1],
        [0.5, 0],
        [0, 0],
        [2, 0]
    ], index = dates, columns = stocks)

    cum_div = dividends.cumsum()
    cum_daily = dividends.sum(axis=1).cumsum()
    
    print(cum_div.div(cum_daily, axis = 0))

def cumulative_returns():
    returns = pd.DataFrame([
        [np.nan, np.nan, np.nan],
        [1.59904743, 1.66397210, 1.67345829],
        [-0.37065629, -0.36541822, -0.36015840],
        [-0.41055669, 0.60004777, 0.00536958],
    ], index = dates, columns = ['A', 'B', 'C'])

    print(returns)

    returns['cum'] = returns.sum(axis = 1)
    returns = (returns + 1).cumprod() - 1

    rets = returns['cum']
    rets += 1
    print(rets) 
    

    returns['expected'] = [np.nan, 5.93647782, -0.57128454, -0.68260542]
    returns['diff'] = abs(returns['expected']) - abs(returns['cum'])
    print(returns)


def basis_looping():
    returns = pd.DataFrame([
        [np.nan, np.nan, np.nan],
        [1.59904743, 1.66397210, 1.67345829],
        [-0.37065629, -0.36541822, -0.36015840],
        [-0.41055669, 0.60004777, 0.00536958],
        [1.59904743, 1.66397210, 1.67345829],
        [-0.37065629, -0.36541822, -0.36015840],
        [-0.41055669, 0.60004777, 0.00536958],
    ], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
     , columns = ['A', 'B', 'C'])

    print(returns)
    #print(returns.index)
    #print(returns.values)
    print('*******************************')
    print(returns.iloc[-4:1])
    print(returns.loc['e'])

if __name__ == '__main__':
    #index_weights()
    #dividends_weights()
    #cumulative_returns()
    basis_looping()

# %%

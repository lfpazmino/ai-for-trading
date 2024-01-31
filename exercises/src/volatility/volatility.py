#%%
import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # TODO: Fill in this function.
    a = prices[(prices.ticker == 'A')]
    b = prices[(prices.ticker == 'B')]
    
    print(f'A volatility: {a.price.std():.4}')
    print(f'B volatility: {b.price.std():.4}')
    
    if (a['price'].std() > b['price'].std()):
        return 'A'
    else: 
        return 'B'
    #pass


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()

# %%

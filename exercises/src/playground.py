#%%

import pandas as pd

df = pd.DataFrame([1,2,3,4,5], 
                  ['a','b','c','d','e'],
                  [6,7,8,9,0])
print(df)
print('values', df.values)
print('index', df.index)
# %%

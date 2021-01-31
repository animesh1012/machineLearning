import numpy as np
import pandas as pd
def function(p,d=100):
    dt_index = pd.date_range(start='2000-01-01',end='2000-12-01')
    s=d
    df = pd.Series([s if i==0 else s+np.random.binomial(1, p) for i in range(len(dt_index))],index=dt_index)
    return(df)
print(function(0.6,250))

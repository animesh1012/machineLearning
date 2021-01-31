import pandas as pd
n = int(input())
ds = pd.Series([i**2-1 if i%3!=0 else 0 for i in range(1,n+1)],index=[i for i in range(0,2*n,2)])
print(ds)

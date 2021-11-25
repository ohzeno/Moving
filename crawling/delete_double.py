import pandas as pd
import numpy as np

df = pd.read_csv('movies_slice.csv')
df = df.drop_duplicates(subset=['id'], keep='first', inplace=False, ignore_index=False)
# df.to_csv('movies2.csv')
print('끝')
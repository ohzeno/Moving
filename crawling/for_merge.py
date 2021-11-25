import pandas as pd
import numpy as np

df2 = pd.read_csv('movies2.csv', index_col='id')

# print(df['backdrop_path'][1039])
# df = df.dropna(axis=0)
# df.to_csv('movies.csv')
# dfs = [df1, df2]
#
#
# df_fin = pd.concat(dfs)
# df_fin = df_fin.sort_index()
# df_fin = df_fin.dropna(axis=0)
# df_fin.to_csv('movies2.csv')
print(df2['release_date'])
df2['release_date'] = pd.to_datetime(df2['release_date'])
print(df2['release_date'])
df3 = df2.sort_values(by=['release_date'], ascending=[False])
df_slice = df3.iloc[0:2000]
df_slice.to_csv('movies_slice.csv')
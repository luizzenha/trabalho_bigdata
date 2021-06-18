import pandas as pd

df = pd.read_csv("tempo-pavimento-vit.csv", sep=',', header=0, encoding='latin_1')

df2 = df[['pavimento','desc_tempo','num_vitimas']].groupby(['pavimento','desc_tempo'], as_index=True).sum()

df2.plot.barh(y='num_vitimas', figsize=(50, 30))
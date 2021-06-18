import pandas as pd

df = pd.read_csv("veiculo-pavimento-vit.csv", sep=',', header=0, encoding='latin_1')

df2 = df[['pavimento','especie_veiculo','num_vitimas']].groupby(['pavimento','especie_veiculo'], as_index=True).sum()


df2.plot.barh(y='num_vitimas', figsize=(50, 30))
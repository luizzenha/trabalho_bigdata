import pandas as pd

df = pd.read_csv("veiculos-tipoAcidente-vit.csv", sep=',', header=0, encoding='latin_1')

df2 = df[['desc_tipo_acidente','especie_veiculo','num_vitimas']].groupby(['desc_tipo_acidente','especie_veiculo'], as_index=True).sum()


df2.plot.barh(y='num_vitimas', figsize=(50, 200))
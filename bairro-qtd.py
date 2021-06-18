import pandas as pd

df = pd.read_csv("bairro-qtd.csv", sep=',', header=0, encoding='latin_1')

df.plot.bar(x='BAIRRO', y='QUANTIDADE', figsize=(50, 30))

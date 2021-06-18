import pandas as pd

df = pd.read_csv("media-embriaguez.csv", sep=',', header=0, encoding='latin-1')
df.index = list(df["Embreagues"])

df.plot.barh( y='media_idade',  figsize=(10, 10))
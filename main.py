import pandas as pd
import csv

df = pd.read_csv("merge.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
print(df.shape)

df.to_csv("final.csv")

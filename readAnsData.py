import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./database/dados.csv')
print(df)

print(df.head())
print(df.info())
print(df.describe())



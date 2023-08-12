import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./database/dados.csv')

sns.countplot(data=df, x='regiao')
plt.xlabel('Região')
plt.ylabel('Quantidade de Beneficiários')
plt.title('Distribuição de Beneficiários por Região')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./database/dados.csv')

# Agrupamento por região e plano
grupo_regiao_plano = df.groupby(['regiao', 'plano']).size().unstack()

# Plotagem do gráfico de barras agrupado
grupo_regiao_plano.plot(kind='bar', stacked=True)
plt.xlabel('Região')
plt.ylabel('Número de Beneficiários')
plt.title('Distribuição de Beneficiários por Região e Plano de Saúde')
plt.legend(title='Plano')
plt.xticks(np.arange(len(grupo_regiao_plano)), grupo_regiao_plano.index)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./database/dados.csv')

# Contagem de beneficiários por gênero
contagem_genero = df['genero'].value_counts()

# Cores personalizadas em formato RGB normalizado
azul = '#6495ED'  # Azul
rosa = '#FF69B4'  # Rosa

# Plotagem do gráfico de barras
plt.bar(contagem_genero.index, contagem_genero.values, color=[azul, rosa])
plt.xlabel('Gênero')
plt.ylabel('Número de Beneficiários')
plt.title('Distribuição de Beneficiários por Gênero')
plt.show()

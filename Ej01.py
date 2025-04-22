import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo Seaborn
sns.set_theme(style="darkgrid")

# Cargar datos
df = pd.read_csv("recipeData2.csv", sep=';', skipinitialspace=True)

# Limpiar y convertir
cols = ['ABV', 'IBU', 'Color']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df['BrewMethod'] = df['BrewMethod'].str.strip()
df = df.dropna(subset=cols + ['BrewMethod'])

# Agrupar por método de elaboración y sacar promedios
grouped = df.groupby('BrewMethod')[cols].mean()

# Ordenar los métodos por ABV promedio para estética
grouped = grouped.sort_values(by='ABV')

# Gráfico de área
plt.figure(figsize=(12, 6))

plt.fill_between(grouped.index, grouped['ABV'], alpha=0.4, label='ABV (Alcohol %)', color='skyblue')
plt.plot(grouped.index, grouped['ABV'], color='blue')

plt.fill_between(grouped.index, grouped['IBU'], alpha=0.4, label='IBU (Amargor)', color='salmon')
plt.plot(grouped.index, grouped['IBU'], color='red')

plt.fill_between(grouped.index, grouped['Color'], alpha=0.4, label='Color (SRM)', color='khaki')
plt.plot(grouped.index, grouped['Color'], color='goldenrod')

# Personalización
plt.title('Promedio de ABV, IBU y Color según método de elaboración', fontsize=14, weight='bold')
plt.xlabel('Método de Elaboración')
plt.ylabel('Promedio')
plt.legend()
plt.tight_layout()
plt.show()

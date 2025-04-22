import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer CSV (especificando separador)
df = pd.read_csv('recipeData2.csv', sep=';', skipinitialspace=True)

# Reemplazar valores no numéricos y convertir a tipo numérico
df['BoilSize'] = pd.to_numeric(df['BoilSize'], errors='coerce')
df['BoilTime'] = pd.to_numeric(df['BoilTime'], errors='coerce')
df['BrewMethod'] = df['BrewMethod'].str.strip()  # Limpia espacios

# Agrupar por método de elaboración y contar promedios de BoilSize y BoilTime
df_grouped = df.groupby('BrewMethod')[['BoilSize', 'BoilTime']].mean().reset_index()

# Ordenar por BoilSize
df_grouped = df_grouped.sort_values(by='BoilSize', ascending=False)

# Gráfico con seaborn y matplotlib
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# Gráfico de área apilado: BoilSize
plt.fill_between(df_grouped['BrewMethod'], df_grouped['BoilSize'], color='skyblue', alpha=0.4, label='BoilSize')
plt.plot(df_grouped['BrewMethod'], df_grouped['BoilSize'], marker='o', color='blue', linewidth=2)

# Gráfico de área apilado: BoilTime
plt.fill_between(df_grouped['BrewMethod'], df_grouped['BoilTime'], color='lightgreen', alpha=0.4, label='BoilTime')
plt.plot(df_grouped['BrewMethod'], df_grouped['BoilTime'], marker='o', color='green', linewidth=2)



# Personalización
plt.title('Promedio de Tamaño y Tiempo de Hervor por Método de Elaboración', fontsize=14)
plt.xlabel('Método de Elaboración')
plt.ylabel('Valor Promedio')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

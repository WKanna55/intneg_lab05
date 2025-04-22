import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos desde el CSV
file_path = "recipeData2.csv"
df = pd.read_csv(file_path, delimiter=";")

# Asegurarse de que las columnas relevantes están en el formato correcto
df['ABV'] = pd.to_numeric(df['ABV'], errors='coerce')
df['IBU'] = pd.to_numeric(df['IBU'], errors='coerce')
df['StyleID'] = df['StyleID'].astype(str)

# Agrupar por estilo de cerveza y calcular la media de ABV e IBU
grouped = df.groupby('StyleID').agg({'ABV': 'mean', 'IBU': 'mean'}).reset_index()

# Estilizar el gráfico con un fondo más atractivo y colores vibrantes
sns.set(style="whitegrid", palette="dark:#5A9_r", rc={"axes.facecolor": "#F4F4F9", "axes.grid": True})

# Crear un gráfico de dispersión para ABV vs IBU con regresión y fondo más trabajado
plt.figure(figsize=(14, 10))
scatter_plot = sns.scatterplot(data=grouped, x='IBU', y='ABV', hue='StyleID', palette='viridis', s=150, edgecolor='black', linewidth=1.2, marker='o')

# Añadir una línea de regresión para mostrar la tendencia general
sns.regplot(data=grouped, x='IBU', y='ABV', scatter=False, color='gray', line_kws={'linewidth': 2, 'linestyle': '--', 'color': 'black'})

# Estilizar los ejes y etiquetas
scatter_plot.set_title('Relación entre ABV y IBU por Estilo de Cerveza', fontsize=20, weight='bold', color='#3F3F3F')
scatter_plot.set_xlabel('IBU (Unidades amargas)', fontsize=14, weight='bold', color='#3F3F3F')
scatter_plot.set_ylabel('ABV (Alcohol por volumen)', fontsize=14, weight='bold', color='#3F3F3F')

# Mejorar la legibilidad de la leyenda
plt.legend(title='Estilo de Cerveza', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12, title_fontsize=14)

# Ajustes adicionales para mejorar el diseño
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Mostrar el gráfico
plt.show()

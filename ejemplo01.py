import pandas as pd
import matplotlib.pyplot as plt

# Datos de prueba
data = {
    'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
    'Producto A': [100, 120, 140, 130, 160],
    'Producto B': [80, 90, 100, 110, 120],
    'Producto C': [60, 70, 65, 80, 90]
}

df = pd.DataFrame(data)
df01 = pd.read_csv('recipeData2.csv')

# Relleno individual por producto (no apilado)
plt.figure(figsize=(10, 6))

plt.fill_between(df['Mes'], df['Producto A'], alpha=0.4, label='Producto A')
plt.plot(df['Mes'], df['Producto A'], color='blue')

plt.fill_between(df['Mes'], df['Producto B'], alpha=0.4, label='Producto B')
plt.plot(df['Mes'], df['Producto B'], color='orange')

plt.fill_between(df['Mes'], df['Producto C'], alpha=0.4, label='Producto C')
plt.plot(df['Mes'], df['Producto C'], color='green')

plt.title('Ventas mensuales por producto (Gráfico de Área)')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.legend()
plt.tight_layout()
plt.show()

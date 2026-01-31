import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# 1. Cargar el dataset correctamente
# -----------------------------
df = pd.read_csv('housing_data500.csv')

# -----------------------------
# 2. Limpieza perfecta de las columnas numéricas
# -----------------------------
# Precio: "$2,500,000" → 2500000.0
df['Sale price'] = (
    df['Sale price']
    .replace(r'[\$,]', '', regex=True)   # quita $ y comas
    .astype(float)
)

# Metros cuadrados: "3,200" → 3200.0 (las comillas son parte del CSV)
df['Square footage'] = (
    df['Square footage']
    .replace(r'[",]', '', regex=True)    # quita comillas dobles y comas
    .astype(float)
)

# -----------------------------
# 3. Gráfico de barras: Precio promedio por número de dormitorios
# -----------------------------
plt.figure(figsize=(11, 6))
sns.barplot(
    data=df,
    x='Number of bedrooms',
    y='Sale price',
    #estimator='mean',       # puedes cambiar a 'median' si querés menos influencia de mansiones
    estimator='median',
    errorbar='sd',          # barras de error = desviación estándar
    palette='viridis',
    edgecolor='black',
    linewidth=1.2,
    alpha=0.9
)

plt.title('Precio promedio de venta por número de dormitorios', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Número de dormitorios', fontsize=13)
plt.ylabel('Precio de venta (USD)', fontsize=13)

# Formato en millones
formatter = plt.FuncFormatter(lambda x, _: f'${x:,.0f}')
plt.gca().yaxis.set_major_formatter(formatter)

plt.grid(axis='y', linestyle='--', alpha=0.6)
sns.despine()

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import mannwhitneyu


#streamlit run testegrafic1.py 
# 1. Crear datos de prueba (Dos grupos independientes)
grupo_A = [20, 22, 19, 24, 25, 28, 21, 23, 22, 26]
grupo_B = [28, 32, 30, 29, 35, 27, 31, 33, 34, 29]

# 2. Calcular el Test U de Mann-Whitney
stat, p_value = mannwhitneyu(grupo_A, grupo_B)
print(f"Estadístico U: {stat}")
print(f"Valor p: {p_value}")

# 3. Preparar los datos para graficar con Seaborn
data = pd.DataFrame(
    {"Valores": grupo_A + grupo_B, "Grupo": ["Grupo A"] * 10 + ["Grupo B"] * 10}
)

# 4. Crear el gráfico (Plot)
plt.figure(figsize=(8, 5))
sns.boxplot(x="Grupo", y="Valores", data=data, palette="Set2", width=0.5)
sns.stripplot(x="Grupo", y="Valores", data=data, color="black", alpha=0.5, size=6)

# Añadir títulos e información estadística al gráfico
plt.title("Prueba U de Mann-Whitney - Comparación de Grupos")
plt.text(
    x=0.5,
    y=max(data["Valores"]) - 1,
    s=f"U = {stat:.1f}\np-value = {p_value:.4f}",
    ha="center",
    va="center",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.7),
)

# Mostrar el gráfico en el navegador
plt.show()
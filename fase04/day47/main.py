import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

dates = {
    "Producto": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "Región": ["Norte", "Norte", "Norte", "Sur", "Sur", "Sur", "Este", "Este", "Este", "Oeste", "Oeste", "Oeste"],
    "Ventas": [120, 150, 90, 200, 180, 140, 160, 170, 130, 100, 110, 80],
    "Costo": [70, 90, 50, 130, 110, 85, 100, 105, 95, 60, 70, 45],
    "Mes": ["Enero", "Enero", "Enero", "Febrero", "Febrero", "Febrero", "Marzo", "Marzo", "Marzo", "Abril", "Abril", "Abril"]
}

df = pd.DataFrame(dates)

sns.barplot(data=df, x="Producto", y="Ventas", errorbar=None)
plt.title("Ventas por Producto")
plt.show()

sns.barplot(data=df, x="Producto", y="Ventas", hue="Región")
plt.title("Ventas por Producto y Región")
plt.show()

sns.boxplot(data=df, x="Producto", y="Ventas")
plt.title("Distribución de Costos por Producto")
plt.show()

corr = df[["Ventas", "Costo"]].corr()
sns.heatmap(corr, annot=True, cmap="YlGnBu")
plt.title("Correlación Ventas vs Costo")
plt.show()

sns.lineplot(data=df, x="Mes", y="Ventas", hue="Producto", marker="o")
plt.title("Tendencia de Ventas por Mes")
plt.show()
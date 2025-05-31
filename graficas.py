import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos del classification report
data = {
    "Clase": [
        "Crisis hipertensiva", "Hipertensión grado 1", "Hipertensión grado 2",
        "Normotensión", "Presión elevada"
    ],
    "Precision": [0.78, 0.89, 0.79, 0.89, 1.00],
    "Recall": [0.58, 0.70, 0.92, 1.00, 0.50],
    "F1-score": [0.67, 0.78, 0.85, 0.94, 0.67],
    "Support": [12, 23, 53, 8, 4]
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Derretir para graficar con seaborn
df_melt = df.melt(id_vars="Clase", value_vars=["Precision", "Recall", "F1-score"],
                  var_name="Métrica", value_name="Valor")

# Estilo
sns.set(style="whitegrid")

# Crear gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=df_melt, x="Clase", y="Valor", hue="Métrica", palette="Set2")

# Ajustar detalles
plt.title("Clasificación por Tipo de Hipertensión", fontsize=14)
plt.ylabel("Valor")
plt.xticks(rotation=30, ha='right')
plt.ylim(0, 1.05)
plt.legend(title="Métrica")
plt.tight_layout()

# Mostrar gráfico
plt.show()

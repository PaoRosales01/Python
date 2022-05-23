# Universidad Tecnológica de Durango
# Por: Paola Elizabeth Rosales Verdín
# Fecha: 28/03/2022
# Materia: Administración de Bases de Datos

import pandas as pd
import matplotlib.pyplot as plt

#crosstab
#Agregar el archivo para análisis con pandas
df = pd.read_csv('usuarios_completo.csv')
#Seleccionar las columnas a procesar
df = df[['gender', 'department']]
#Crear un cruce entre columnas y filas
ct = pd.crosstab(df['gender'], df['department']).plot(kind='bar')
plt.title('Gráfica para cruce de género y departamento')
plt.xlabel("Género")
plt.ylabel("Departamento")
for barra in ct.containers:
    ct.bar_label(barra,label_type='edge')
    
#plt.legend(loc='lower left')
plt.legend(loc='best')
plt.savefig(fname='crosstab.png', dpi=600, bbox_inches='tight', pad_inches=0.5)

    
plt.show()

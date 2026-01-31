#Importemos algunas de las librerías más clásicas para el manejo de datos en Python

#Pandas es la librería básica para la manipulación y análisis de datos
import pandas as pd

#Numpy es la biblioteca para crear vectores y matrices, además de un conjunto grande de funciones matemáticas
import numpy as np

#Seaborn es una librería que usamos para graficar
import seaborn as sns

#Statsmodels es la biblioteca para realizar modelos
import statsmodels.formula.api as smf

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1")

print(df_nations)
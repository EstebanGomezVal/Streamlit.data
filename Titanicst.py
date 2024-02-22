# Instalar librerias 

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Visualización del Titanic")
st.header("Data set")
st.markdown("*Este es una base de datos acerca del Titanic*")

# Importar csv
data = ("Titanic-Dataset.csv")
df = pd.read_csv(data)
df


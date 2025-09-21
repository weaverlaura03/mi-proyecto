import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Sprint 7 — Dashboard de Vehículos")

# Cargar dataset real (debe existir en la raíz del repo)
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
if st.button('Mostrar histograma'):
    st.write("Histograma del odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión'):
    st.write("Precio vs Odómetro")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Vehiculos", anchor=None,  help=None)
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

if st.button('Mostrar Histograma'):  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer") # crear un histograma

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if st.button('Mostrar Gráfico de dispersión'):  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price") 

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

  # crear un gráfico de histograma
#fig.show()
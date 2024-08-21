import pandas as pd
import plotly.express as px
import streamlit as st
#crear el encabezado

st.header('Gráficos')
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón  #escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
     # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
fig = px.histogram(car_data, x="odometer") # crear un histograma
fig.show()

import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig.show()

@st.cache
def load_data():
    # Cambia 'data.csv' por la ruta de tu archivo CSV
    df = pd.read_csv('vehicles_us.csv')
    return df

# Cargar los datos
data = load_data()

# Mostrar el encabezado
st.header('Lista de Modelos')

# Asegúrate de que la columna 'model' existe en el archivo CSV
if 'model' in data.columns:
    # Obtener la lista de modelos
    models = data['model'].tolist()
    
    # Mostrar la lista en Streamlit
    st.write('Modelos disponibles:')
    st.write(models)
else:
    st.error('La columna "model" no se encuentra en el archivo CSV.')

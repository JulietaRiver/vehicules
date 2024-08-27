import pandas as pd
import plotly.express as px
import streamlit as st

# Ensure you have the latest Streamlit version
st.write(f"Streamlit version: {st.__version__}")

@st.cache_data(ttl=3600)
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
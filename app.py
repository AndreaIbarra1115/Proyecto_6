import pandas as pd
import plotly.express as px
import streamlit as st
pd.set_option('display.max_columns', None)

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Anuncios de Ventas de Coches')
st.write('''Esta es una aplicación que construye dos gráficos diferentes. El primero es un histograma,
         mientras que el segundo es un diagrama de dispersión. Ambos gráficos se deben de crear
         al momento de hacer clic en cada botón. Los gráficos se crean por separado.''')


hist_button = st.button('Construir histograma')  # crear un botón
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if scatter_button:

    st.write('Creacion de un diagrama de dispersión')

    fig = px.scatter(car_data, x='odometer' y='price')

    st.plotly_chart(fig, use_container_width=True)


import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us_clean.csv') # leer los datos
st.header('Cuadro de Mandos de Anuncios de Vehículos')
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # ecribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
# Botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el precio vs kilometraje')

    # Crear el gráfico de dispersión
    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Relación entre Precio y Kilometraje',
        labels={'odometer': 'Kilometraje', 'price': 'Precio'},
        color='condition',  # Diferenciar por condición del vehículo
        hover_data=['model_year', 'fuel']  # Mostrar datos adicionales al pasar el ratón
    )

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)
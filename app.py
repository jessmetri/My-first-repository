import streamlit as st
import numpy as np
import pandas as pd
import time

# Título de la aplicación
st.header('Lanzamiento de una moneda')

# Control deslizante para definir el número de intentos
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)

# Botón para ejecutar el experimento
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso...')

    # Simulación del lanzamiento de monedas (0 = cara, 1 = cruz)
    resultados = np.random.randint(0, 2, size=number_of_trials)
    media_resultados = np.mean(resultados)

    # Mostrar progreso
    progress_bar = st.progress(0)
    for i in range(1, 101):
        time.sleep(0.02)  # Simula el proceso
        progress_bar.progress(i)

    # Mostrar resultados
    st.subheader('Resultados:')
    st.write(f'La media de los lanzamientos es: {media_resultados:.2f}')

    # Gráfico de progreso
    st.line_chart(pd.DataFrame({'Lanzamientos': np.cumsum(resultados) / np.arange(1, number_of_trials + 1)}))

    # Mostrar los datos en tabla
    df = pd.DataFrame({'Intento': np.arange(1, number_of_trials + 1), 'Resultado': resultados})
    st.dataframe(df)
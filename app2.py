# Librerias
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Datos
df = pd.read_csv("https://raw.githubusercontent.com/jsaraujott/datos/refs/heads/main/iris.csv")

# Titulo
st.header('Relación de variables', divider = "gray")

# Boton Descargar
st.download_button(
    label = "Descargar dataset", 
    data = df.to_csv(index=False), 
    file_name = "df.csv"
)

st.divider()

# Seleccionador de variables
opciones = list(df.columns)[0:4]
v = st.multiselect(
    label = "Seleccione máximo 2 variables:",
    options = opciones,
    max_selections = 2
)

try:

    c1, c2 = st.columns(2)

    with c1: 
        hist_plot01 = px.histograma(data_frame = df, x = v(0), color = 'type') 
        st.plotly_chart(hist_plot01)

        prom1 = np.mean(df[v[0]])
        st.metric(
            label = 'Media',
            value = '{}'.format(round(prom1,1))
        )

    with c2: 
        hist_plot02 = px.histograma(data_frame = df, x = v(1), color = 'type') 
        st.plotly_chart(hist_plot02)

        prom2 = np.mean(df[v[0]])
        st.metric(
            label = 'Media',
            value = '{}'.format(round(prom2,1))
        )

except:

    st.write("Faltan variables por seleccionar")
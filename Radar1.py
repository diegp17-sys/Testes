import streamlit as st
import plotly.graph_objects as go
import pandas as pd


    # Ejemplo de datos de ejemplo
df = pd.DataFrame({
    'Eje': ['Mat int', 'S espa', 'S ', 'Inteligencia', 'Carisma'],
    'Valor': [5, 0, 5, 4, 3],
    'Valor 2': [4, 0, 3, 4, 5]
})


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
        r=df['Valor'],
        theta=df['Eje'],
        fill='toself',
        name='Grupo 1'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 2'],
        theta=df['Eje'],
        fill='toself',
        name='Grupo 2'
    ))
fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )),
        showlegend=True
    )

st.plotly_chart(fig, use_container_width=True)

#streamlit run Radar1.py  
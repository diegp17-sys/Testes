import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

# from PIL import Image
st.set_page_config(layout="wide")
#...matrizes
mz1 = np.zeros((1,7))

#mz1[0,0]=1
#....Diretrizes de Inserção
st.title("Diretrizes de Inserção")
#.....Posicionamento
choice1 = st.selectbox('Para diretrizes de posicionamento escolha a TE asociadas',[' ','TP 10 Evolução geométrica linear','TP 11 Evolução geométrica volumétrica','TP 12 Dinamização']) 
if choice1 == 'TP 10 Evolução geométrica linear':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE10.gif", caption="Figura 1 - TE 10", width=400)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=300)
    #...selecionar etapas
    etapas=['1','2','3','4','5']
    choicem = st.select_slider('Etapa atual:', options=etapas)
    st.write("A etapa é: ",choicem)

    mz1[0,0]='10'
    mz1[0,6]=choicem
    if choicem == '1':
        mz1[0,1]=1
    if choicem == '2':
        mz1[0,2]=1
    if choicem == '3':
        mz1[0,3]=1 
    if choicem == '4':
        mz1[0,4]=1
    if choicem == '5':
        mz1[0,5]=1
    np.save(file = 'TE1', arr=mz1) 
    #.....fim etapas
if choice1 == 'TP 11 Evolução geométrica volumétrica':
    st.write("Descrição:.... "
             "Aumenta:....") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE11.gif", caption="Figura 1 - TE 11", width=300)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=300)
    #...selecionar etapas
    etapas=['1','2','3','4','5']
    choicem2 = st.select_slider('Etapa atual:', options=etapas)
    st.write("A etapa é: ",choicem2)
    mz1[0,0]='11'
    mz1[0,6]=choicem2
    if choicem2 == '1':
        mz1[0,1]=1
    if choicem2 == '2':
        mz1[0,2]=1
    if choicem2 == '3':
        mz1[0,3]=1 
    if choicem2 == '4':
        mz1[0,4]=1
    if choicem2 == '5':
        mz1[0,5]=1
    np.save(file = 'TE11', arr=mz1) 
    #.....fim etapas
if choice1 == 'TP 12 Dinamização':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE12.gif", caption="Figura 1 - TE 12", width=400)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=300)
    #...selecionar etapas
    etapas1=['1','2','3','4','5']
    choicem1 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem1)
    mz1[0,0]=12
    mz1[0,6]=choicem1
    if choicem1 == '1':
        mz1[0,1]=1
    if choicem1 == '2':
        mz1[0,2]=1
    if choicem1 == '3':
        mz1[0,3]=1 
    if choicem1 == '4':
        mz1[0,4]=1 
    if choicem1 == '5':
        mz1[0,5]=1
    np.save(file = 'TE2', arr=mz1) 
    #.....fim etapas
#.....Alinhamento
choice1 = st.selectbox('Para diretrizes de alinhamento escolha a TE asociadas',[' ','TEA 10 Evolução geométrica linear','TEA 11 Evolução geométrica volumétrica','TEA 12 Dinamização']) 
if choice1 == 'TEA 10 Evolução geométrica linear':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    st.image("TE10.gif", caption="Figura 1 - TE 10", width=700)
    st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=700)
if choice1 == 'TEA 11 Evolução geométrica volumétrica':
    st.write("Descrição:.... "
             "Aumenta:....") 
    st.image("TE11.gif", caption="Figura 1 - TE 11", width=700)
    st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=700)
if choice1 == 'TEA 12 Dinamização':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    st.image("TE12.gif", caption="Figura 1 - TE 12", width=700)
    st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=700)
#...
choice2 = st.selectbox('Para diretrizes de orientacao e simetria escolha a TE asociada',[' ','TA1','TA2','TA3']) 
if choice2 == 'TA1':
    st.write("Descricao.... "
             "etapas!") 
    st.image("TE1.gif", caption="figura 1 ", width=500)
if choice2 == 'TA2':
    st.write("Descricao.... "
             "etapas!") 
    st.image("TE2.gif", caption="figura 1 ", width=500)

#...



#....Diretrizes de fixação
st.title("Diretrizes de fixação")
#.....Posicionamento
choice1 = st.selectbox('Para diretrizes do tipo de fixadores escolha a TE asociadas',[' ','TP 10 Evolução geométrica linear','TP 11 Evolução geométrica volumétrica','TP 12 Dinamização']) 
if choice1 == 'TP 10 Evolução geométrica linear':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    st.image("TE10.gif", caption="Figura 1 - TE 10", width=700)
    st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=700)
if choice1 == 'TP 11 Evolução geométrica volumétrica':
    st.write("Descrição:.... "
             "Aumenta:....") 
    st.image("TE11.gif", caption="Figura 1 - TE 11", width=700)
    st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=700)
if choice1 == 'TP 12 Dinamização':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    st.image("TE12.gif", caption="Figura 1 - TE 12", width=700)
    st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=700)

#st.write(mz1) 
#etapasmatriz = ['TE / Etapas','1','2','3','4','5']
st.write("TE     Estagios")
vetorte1 = np.load(file = 'TE1.npy')
st.write("TE 10.",vetorte1)
vetorte2 = np.load(file = 'TE2.npy')
st.write("TE 12",vetorte2)
vetorte3 = np.load(file = 'TE11.npy')
st.write("TE 11.",vetorte3)
matriz = np.vstack([vetorte1, vetorte2, vetorte3, vetorte3])
st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
val=matriz[:,6]
st.write("Vlor de cada tendencia",val)
#...graf radar
df = pd.DataFrame({
    'Eje': ['Mat inteligentes', 'S espaço', 'S super', 'S. objeto'],
    #'Valor': [5, 0, 5, 4],
    'Valor': val,
    #'Valor 2': [4, 0, 3, 4, 5]
})


fig = go.Figure()
fig.add_trace(go.Scatterpolar(
        r=df['Valor'],
        theta=df['Eje'],
        fill='toself',
        #name='Grupo 1'
    ))
#fig.add_trace(go.Scatterpolar(
#        r=df['Valor 2'],
#        theta=df['Eje'],
#        fill='toself',
#        name='Grupo 2'
#    ))
fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )),
        showlegend=True
    )

st.plotly_chart(fig, use_container_width=True)


#streamlit run teste5.py  
#pip freeze > requirements.txt
#pip show plotly


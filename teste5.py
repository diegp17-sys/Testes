import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

# from PIL import Image
st.set_page_config(layout="wide")
#...matrizes
mz1 = np.zeros((1,8))
mz2 = np.zeros((1,8))
mz3 = np.zeros((1,8))
#mz1[0,0]=1
#....Diretrizes de Inserção
st.title("Diretrizes de Inserção")
#.....Posicionamento
choice1 = st.selectbox('Para diretrizes de posicionamento escolha a TE asociadas',[' ','TP 10 Evolução geométrica linear','TP 11 Evolução geométrica volumétrica','TP 12 Dinamização','TP 13 – Coordenação das ações','TP 16 – Combinar sistemas similares','TP 17 – Combinar sistemas diversos','TP 18 – Combinar sistemas diferentes']) 
if choice1 == 'TP 10 Evolução geométrica linear':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE10.gif", caption="Figura 1 - TE 10", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas=['1','2','3','4','5']
    choicem10 = st.select_slider('Etapa atual:', options=etapas)
    #st.write("A etapa é: ",choicem)
    mz1[0,0]='10'
    mz1[0,6]=choicem10
    if choicem10 == '1':
        mz1[0,1]=1
        mz1[0,7]=101
    if choicem10 == '2':
        mz1[0,2]=1
        mz1[0,7]=102
    if choicem10 == '3':
        mz1[0,3]=1 
        mz1[0,7]=103
    if choicem10 == '4':
        mz1[0,4]=1
        mz1[0,7]=104
    if choicem10 == '5':
        mz1[0,5]=1
        mz1[0,7]=105
    np.save(file = 'TE10', arr=mz1) 
    #.....fim etapas
if choice1 == 'TP 11 Evolução geométrica volumétrica':
    st.write("Descrição:.... "
             "Aumenta:....") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE11.gif", caption="Figura 1 - TE 11", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas=['1','2','3','4','5']
    choicem11 = st.select_slider('Etapa atual:', options=etapas)
    st.write("A etapa é: ",choicem11)
    mz1[0,0]='11'
    mz1[0,6]=choicem11
    if choicem11 == '1':
        mz1[0,1]=1
        mz1[0,7]=111
    if choicem11 == '2':
        mz1[0,2]=1
        mz1[0,7]=112
    if choicem11 == '3':
        mz1[0,3]=1
        mz1[0,7]=113 
    if choicem11 == '4':
        mz1[0,4]=1
        mz1[0,7]=114
    if choicem11 == '5':
        mz1[0,5]=115
    np.save(file = 'TE11', arr=mz1) 
    #.....fim etapas
if choice1 == 'TP 12 Dinamização':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE12.gif", caption="Figura 1 - TE 12", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas1=['1','2','3','4','5']
    choicem12 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem12)
    mz1[0,0]=12
    mz1[0,6]=choicem12
    if choicem12 == '1':
        mz1[0,1]=1
    if choicem12 == '2':
        mz1[0,2]=1
    if choicem12 == '3':
        mz1[0,3]=1 
    if choicem12 == '4':
        mz1[0,4]=1 
    if choicem12 == '5':
        mz1[0,5]=1
    np.save(file = 'TE12', arr=mz1) 
    #.....fim etapas
# TE13
if choice1 == 'TP 13 – Coordenação das ações':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE13.gif", caption="Figura 1 - TE 13", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas1=['1','2','3','4','5']
    choicem13 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem13)
    mz1[0,0]=13
    mz1[0,6]=choicem13
    if choicem13 == '1':
        mz1[0,1]=1
    if choicem13 == '2':
        mz1[0,2]=1
    if choicem13 == '3':
        mz1[0,3]=1 
    if choicem13 == '4':
        mz1[0,4]=1 
    if choicem13 == '5':
        mz1[0,5]=1
    np.save(file = 'TE13', arr=mz1) 
    #.....fim etapas

# TE16
if choice1 == 'TP 16 – Combinar sistemas similares':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE16.gif", caption="Figura 1 - TE 16", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas1=['1','2','3','4','5']
    choicem16 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem16)
    mz1[0,0]=16
    mz1[0,6]=choicem16
    if choicem16 == '1':
        mz1[0,1]=1
    if choicem16 == '2':
        mz1[0,2]=1
    if choicem16 == '3':
        mz1[0,3]=1 
    if choicem16 == '4':
        mz1[0,4]=1 
    if choicem16 == '5':
        mz1[0,5]=1
    np.save(file = 'TE16', arr=mz1) 
    #.....fim etapas


# TE17
if choice1 == 'TP 17 – Combinar sistemas diversos':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE17.gif", caption="Figura 1 - TE 16", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas1=['1','2','3','4','5']
    choicem17 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem17)
    mz1[0,0]=17
    mz1[0,6]=choicem17
    if choicem17 == '1':
        mz1[0,1]=1
    if choicem17 == '2':
        mz1[0,2]=1
    if choicem17 == '3':
        mz1[0,3]=1 
    if choicem17 == '4':
        mz1[0,4]=1 
    if choicem17 == '5':
        mz1[0,5]=1
    np.save(file = 'TE17', arr=mz1) 
    #.....fim etapas

# TE18
if choice1 == 'TP 18 – Combinar sistemas diferentes':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE18.gif", caption="Figura 1 - TE 16", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas1=['1','2','3','4','5']
    choicem18 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem18)
    mz1[0,0]=18
    mz1[0,6]=choicem18
    if choicem18 == '1':
        mz1[0,1]=1
    if choicem18 == '2':
        mz1[0,2]=1
    if choicem18 == '3':
        mz1[0,3]=1 
    if choicem18 == '4':
        mz1[0,4]=1 
    if choicem18 == '5':
        mz1[0,5]=1
    np.save(file = 'TE18', arr=mz1) 
#.....fim etapas

#..............................................................................................
#..........................diretrizes de Alinhamento............................................
choice2 = st.selectbox('Para diretrizes de alinhamento escolha a TE asociadas',[' ','TEA 12 - Dinamizar','TEA 15 - Casamento com não-linearidades externas','TEA 16 – Combinar sistemas similares','TEA 17 – Combinar sistemas diversos','TEA 18 – Combinar sistemas diferentes'],) 
if choice2 == 'TEA 12 - Dinamizar':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE12.gif", caption="Figura 1 - TE 12", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de alinhamento", width=600)
    #...selecionar etapas
    etapasa=['1','2','3','4','5']
    choicema12 = st.select_slider('Etapa atual do alinhmanto:', options=etapasa)
    #st.write("A etapa é: ",choicem)
    mz2[0,0]='12'
    mz2[0,6]=choicema12
    if choicema12 == '1':
        mz2[0,1]=1
    if choicema12 == '2':
        mz2[0,2]=1
    if choicema12 == '3':
        mz2[0,3]=1 
    if choicema12 == '4':
        mz2[0,4]=1
    if choicema12 == '5':
        mz2[0,5]=1
    np.save(file = 'TEA12', arr=mz2) 
    #.....fim etapas
 

if choice2 == 'TEA 15 - Casamento com não-linearidades externas':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE15.gif", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de alinhamento", width=600)
    #...selecionar etapas
    etapasa=['1','2','3','4','5']
    choicema15 = st.select_slider('Etapa atual do alinhmanto:', options=etapasa)
    #st.write("A etapa é: ",choicem)
    mz2[0,0]='15'
    mz2[0,6]=choicema15
    if choicema15 == '1':
        mz2[0,1]=1
    if choicema15 == '2':
        mz2[0,2]=1
    if choicema15 == '3':
        mz2[0,3]=1 
    if choicema15 == '4':
        mz2[0,4]=1
    if choicema15 == '5':
        mz2[0,5]=1
    np.save(file = 'TEA15', arr=mz2) 
    #.....fim etapas

if choice2 == 'TEA 16 – Combinar sistemas similares':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE16.gif", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de alinhamento", width=600)
    #...selecionar etapas
    etapasa=['1','2','3','4','5']
    choicema16 = st.select_slider('Etapa atual do alinhmanto:', options=etapasa)
    #st.write("A etapa é: ",choicem)
    mz2[0,0]='16'
    mz2[0,6]=choicema16
    if choicema16 == '1':
        mz2[0,1]=1
    if choicema16 == '2':
        mz2[0,2]=1
    if choicema16 == '3':
        mz2[0,3]=1 
    if choicema16 == '4':
        mz2[0,4]=1
    if choicema16 == '5':
        mz2[0,5]=1
    np.save(file = 'TEA16', arr=mz2) 
    #.....fim etapas


if choice2 == 'TEA 17 – Combinar sistemas diversos':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE17.gif", caption="Figura 1 - TE 17", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de alinhamento", width=700)
    #...selecionar etapas
    etapasa=['1','2','3','4','5']
    choicem17 = st.select_slider('Etapa atual do alinhmanto:', options=etapasa)
    #st.write("A etapa é: ",choicem)
    mz2[0,0]='17'
    mz2[0,6]=choicem17
    if choicem17 == '1':
        mz2[0,1]=1
    if choicem17 == '2':
        mz2[0,2]=1
    if choicem17 == '3':
        mz2[0,3]=1 
    if choicem17 == '4':
        mz2[0,4]=1
    if choicem17 == '5':
        mz2[0,5]=1
    np.save(file = 'TEA17', arr=mz2) 
    #.....fim etapas



if choice2 == 'TEA 18 – Combinar sistemas diferentes':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE18.gif", caption="Figura 1 - TE 18", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de alinhamento", width=700)
    #...selecionar etapas
    etapasa=['1','2','3','4','5']
    choicem18 = st.select_slider('Etapa atual do alinhmanto:', options=etapasa)
    #st.write("A etapa é: ",choicem)
    mz2[0,0]='18'
    mz2[0,6]=choicem18
    if choicem18 == '1':
        mz2[0,1]=1
    if choicem18 == '2':
        mz2[0,2]=1
    if choicem18 == '3':
        mz2[0,3]=1 
    if choicem18 == '4':
        mz2[0,4]=1
    if choicem18 == '5':
        mz2[0,5]=1
    np.save(file = 'TEA18', arr=mz2) 
    #.....fim etapas


#...

#..........................................................................................
#.......................diretrizes de orientacao...........................................
choice3 = st.selectbox('Para diretrizes de orientacao e simetria escolha a TE asociada',[' ','TES Simetria','TES Casamento com não-linearidades externas','TES Aumento do uso da cor']) 
if choice3 == 'TES Simetria':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE8.gif", caption="Figura 1 - TE 12", width=770)
    with cols[2]:
        st.image("DFX_simetria.gif", caption="Figura 3 - Diretrizes de simetria", width=770)
    #...selecionar etapas
    etapass=['1','2','3','4','5']
    choicems8 = st.select_slider('Etapa atual da simetria:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz3[0,0]='8'
    mz3[0,6]=choicems8
    if choicems8 == '1':
        mz3[0,1]=1
    if choicems8 == '2':
        mz3[0,2]=1
    if choicems8 == '3':
        mz3[0,3]=1 
    if choicems8 == '4':
        mz3[0,4]=1
    if choicems8 == '5':
        mz3[0,5]=1
    np.save(file = 'TES8', arr=mz3) 
    #.....fim etapas

if choice3 == 'TES Casamento com não-linearidades externas':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE15.gif", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_simetria.gif", caption="Figura 3 - Diretrizes de simetria", width=770)
    #...selecionar etapas
    etapass=['1','2','3','4','5']
    choicems15 = st.select_slider('Etapa atual da simetria:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz3[0,0]='15'
    mz3[0,6]=choicems15
    if choicems15 == '1':
        mz3[0,1]=1
    if choicems15 == '2':
        mz3[0,2]=1
    if choicems15 == '3':
        mz3[0,3]=1 
    if choicems15 == '4':
        mz3[0,4]=1
    if choicems15 == '5':
        mz3[0,5]=1
    np.save(file = 'TES15', arr=mz3) 
    #.....fim etapas

#TES Aumento do uso da cor
if choice3 == 'TES Aumento do uso da cor':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE21.gif", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_simetria.gif", caption="Figura 3 - Diretrizes de simetria", width=770)
    #...selecionar etapas
    etapass=['1','2','3','4','5']
    choicems21 = st.select_slider('Etapa atual da simetria:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz3[0,0]='21'
    mz3[0,6]=choicems21
    if choicems21 == '1':
        mz3[0,1]=1
    if choicems21 == '2':
        mz3[0,2]=1
    if choicems21 == '3':
        mz3[0,3]=1 
    if choicems21 == '4':
        mz3[0,4]=1
    if choicems21 == '5':
        mz3[0,5]=1
    np.save(file = 'TES21', arr=mz3) 
    #.....fim etapas


#.................................................................................................
#....................................Diretrizes de fixação.........................................
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
Vz = [1,1,1,1,1,1,1,1]

vetorte10 = np.load(file = 'TE10.npy')
vetorte11 = np.load(file = 'TE11.npy')
vetorte12 = np.load(file = 'TE12.npy')
vetorte13 = np.load(file = 'TE13.npy')
vetorte16 = np.load(file = 'TE16.npy')
vetorte17 = np.load(file = 'TE17.npy')
vetorte18 = np.load(file = 'TE18.npy')
matriz1 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetorte10, vetorte11, vetorte12, vetorte13, Vz, vetorte16, vetorte17,vetorte18,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
val=matriz1[:,6]
#st.write("Vlor de cada tendencia",val)

#...
#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]
vetortea12 = np.load(file = 'TEA12.npy')
vetortea15 = np.load(file = 'TEA15.npy')
vetortea16 = np.load(file = 'TEA16.npy')
vetortea17 = np.load(file = 'TEA17.npy')
vetortea18 = np.load(file = 'TEA18.npy')
matriz2 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetortea12,Vz,vetortea15, vetortea16, vetortea17,vetortea18,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
vala=matriz2[:,6]

#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]

vetortes8 = np.load(file = 'TES8.npy')
vetortes15 = np.load(file = 'TES15.npy')
vetortes21 = np.load(file = 'TES21.npy')
matriz3 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetortes8,Vz,Vz,Vz, Vz, Vz, vetortes15, Vz, Vz,Vz,vetortes21])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
vals=matriz3[:,6]

#.....................Grafico de radar
st.title("Gráfico radar do potencial evolucionário")
#...graf radar
df = pd.DataFrame({
    'Eje': ['Mat. inteligentes','Seg. espaço ','S. superfície','S. objeto','Macro/nano','Redes e fibras','Densidade','Assimetria','Linhas divisórias','E. geometria linear', 'E. geométrica volumétrica', 'Dinamizar','Coor. ações', 'Não-linearidades externas', 'Comb. sistemas similares', 'Comb. sistemas diversos','Comb. sistemas diferentes ','cor'],
    'Valor': val,
    'Valor 1': vala,
    'Valor 2': vals,
    #'Valor 2': [4, 0, 3, 4, 5]
})

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
        r=df['Valor'],
        theta=df['Eje'],
        fill='toself',
        name='Posicionamento'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 1'],
        theta=df['Eje'],
        fill='toself',
        name='Alinhamento'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 2'],
        theta=df['Eje'],
        fill='toself',
        name='Simetria'
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
#................fim grafico de radar....

#.............................................
#.............reporte.........................
st.title("Reporte")
#.....Posicionamento
st.write(mz1)


choicer = st.selectbox('Diretrizes para gerar reporte',[' ','Posicionamento','Alinhamento','Simetria']) 

if choicer == 'Posicionamento':
#    st.write("Potencial evolucionario TE10") 
    if matriz1[9,7] == 101:
        st.image("TE10R1.png", width=1000)
    if matriz1[9,7] == 102:
        st.image("TE10R2.png", width=1000)
    if matriz1[9,7] == 103:
        st.image("TE10R3.png", width=1000)
    if matriz1[9,7] == 104:
        st.image("TE10R4.png", width=1000)

#    st.write("Potencial evolucionario TE11") 
    if matriz1[10,7] == 111:
        st.image("TE11R1.png", width=1000)
    if matriz1[10,7] == 112:
        st.image("TE11R2.png", width=1000)
    if matriz1[10,7] == 113:
        st.image("TE11R3.png", width=1000)
    if matriz1[10,7] == 114:
        st.image("TE11R4.png", width=1000)

if choicer == 'Alinhamento':
    st.write("Potencial evolucionario.") 
    if matriz1[10,7] == 111:
        st.image("TE16R1.gif", caption="Figura 1 - TE 10", width=1000)
    if matriz1[10,7] == 112:
        st.image("TE16R2.gif", caption="Figura 1 - TE 10", width=1000)
    if matriz1[10,7] == 113:
        st.image("TE16R3.gif", caption="Figura 1 - TE 10", width=1000)
    if matriz1[10,7] == 114:
        st.image("TE16R4.gif", caption="Figura 1 - TE 10", width=1000)

v=[0]
st.write(v)
v1=[100]
v=v+v1
st.write(v)
#.............fim reporte.................

#....plot matrizes
st.title("Matrizes Tedencias da evolucao vs. Estapas atuais")
st.write("Diretrizes de posicionamento  ",matriz1[:,(0,1,2,3,4,5,6,7)])
st.write("Diretrizes de alinhamento",matriz2[:,(0,1,2,3,4,5,6,7)])
st.write("Diretrizes de simetria",matriz3[:,(0,1,2,3,4,5,6,7)])

#streamlit run teste5.py  
#pip freeze > requirements.txt
#pip show plotly


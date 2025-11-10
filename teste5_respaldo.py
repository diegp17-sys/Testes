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
#............................Posicionamento..............................
choice1 = st.selectbox('Para diretrizes de posicionamento escolha a TE asociadas',[' ','TP 10 Evolução geométrica linear','TP 11 Evolução geométrica volumétrica','TP 12 Dinamização','TP 13 – Coordenação das ações','TP 16 – Combinar sistemas similares','TP 17 – Combinar sistemas diversos','TP 18 – Combinar sistemas diferentes']) 
if choice1 == 'TP 10 Evolução geométrica linear':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE10R0.png", caption="Figura 1 - TE 10", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas=['1','2','3','4']
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

    np.save(file = 'TE10', arr=mz1) 
    #.....fim etapas
if choice1 == 'TP 11 Evolução geométrica volumétrica':
    st.write("Descrição:.... "
             "Aumenta:....") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE11R0.png", caption="Figura 1 - TE 11", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas=['1','2','3','4']
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
    np.save(file = 'TE11', arr=mz1) 
    #.....fim etapas
if choice1 == 'TP 12 Dinamização':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE12R0.png", caption="Figura 1 - TE 12", width=770)
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
        mz1[0,7]=121
    if choicem12 == '2':
        mz1[0,2]=1
        mz1[0,7]=122
    if choicem12 == '3':
        mz1[0,3]=1 
        mz1[0,7]=123
    if choicem12 == '4':
        mz1[0,4]=1 
        mz1[0,7]=124
    if choicem12 == '5':
        mz1[0,5]=1
        mz1[0,7]=125
    np.save(file = 'TE12', arr=mz1) 
    #.....fim etapas
# TE13
if choice1 == 'TP 13 – Coordenação das ações':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE13R0.png", caption="Figura 1 - TE 13", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas1=['1','2','3','4']
    choicem13 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem13)
    mz1[0,0]=13
    mz1[0,6]=choicem13
    if choicem13 == '1':
        mz1[0,1]=1
        mz1[0,7]=131
    if choicem13 == '2':
        mz1[0,2]=1
        mz1[0,7]=132
    if choicem13 == '3':
        mz1[0,3]=1 
        mz1[0,7]=133
    if choicem13 == '4':
        mz1[0,4]=1 
        mz1[0,7]=134
    np.save(file = 'TE13', arr=mz1) 
    #.....fim etapas

# TE16
if choice1 == 'TP 16 – Combinar sistemas similares':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE16R0.png", caption="Figura 1 - TE 16", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas1=['1','2','3','4']
    choicem16 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem16)
    mz1[0,0]=16
    mz1[0,6]=choicem16
    if choicem16 == '1':
        mz1[0,1]=1
        mz1[0,7]=161
    if choicem16 == '2':
        mz1[0,2]=1
        mz1[0,7]=162
    if choicem16 == '3':
        mz1[0,3]=1 
        mz1[0,7]=163
    if choicem16 == '4':
        mz1[0,4]=1 
        mz1[0,7]=164
    np.save(file = 'TE16', arr=mz1) 
    #.....fim etapas


# TE17
if choice1 == 'TP 17 – Combinar sistemas diversos':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE17R0.png", caption="Figura 1 - TE 16", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas1=['1','2','3','4']
    choicem17 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem17)
    mz1[0,0]=17
    mz1[0,6]=choicem17
    if choicem17 == '1':
        mz1[0,1]=1
        mz1[0,7]=171
    if choicem17 == '2':
        mz1[0,2]=1
        mz1[0,7]=172
    if choicem17 == '3':
        mz1[0,3]=1 
        mz1[0,7]=173
    if choicem17 == '4':
        mz1[0,4]=1 
        mz1[0,7]=174
    np.save(file = 'TE17', arr=mz1) 
    #.....fim etapas

# TE18
if choice1 == 'TP 18 – Combinar sistemas diferentes':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE18R0.png", caption="Figura 1 - TE 16", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=600)
    #...selecionar etapas
    etapas1=['1','2','3','4']
    choicem18 = st.select_slider('Etapa atual:', options=etapas1)
    st.write("A etapa é: ",choicem18)
    mz1[0,0]=18
    mz1[0,6]=choicem18
    if choicem18 == '1':
        mz1[0,1]=1
        mz1[0,7]=181
    if choicem18 == '2':
        mz1[0,2]=1
        mz1[0,7]=182
    if choicem18 == '3':
        mz1[0,3]=1 
        mz1[0,7]=183
    if choicem18 == '4':
        mz1[0,4]=1 
        mz1[0,7]=184
    np.save(file = 'TE18', arr=mz1) 
#.....fim etapas

#...................................................................................................
#..........................Diretrizes de Alinhamento................................................
#...................................................................................................
choice2 = st.selectbox('Para diretrizes de alinhamento escolha a TE asociadas',[' ','TEA 15 - Casamento com não-linearidades externas','TEA 16 – Combinar sistemas similares','TEA 17 – Combinar sistemas diversos','TEA 18 – Combinar sistemas diferentes'],) 

if choice2 == 'TEA 15 - Casamento com não-linearidades externas':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE15R0.png", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de alinhamento", width=600)
    #...selecionar etapas
    etapasa=['1','2','3']
    choicema15 = st.select_slider('Etapa atual do alinhmanto:', options=etapasa)
    #st.write("A etapa é: ",choicem)
    mz2[0,0]='15'
    mz2[0,6]=choicema15
    if choicema15 == '1':
        mz2[0,1]=1
        mz2[0,7]=151
    if choicema15 == '2':
        mz2[0,2]=1
        mz2[0,7]=152
    if choicema15 == '3':
        mz2[0,3]=1 
        mz2[0,7]=153
    np.save(file = 'TEA15', arr=mz2) 
    #.....fim etapas

if choice2 == 'TEA 16 – Combinar sistemas similares':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE16R0.png", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de alinhamento", width=600)
    #...selecionar etapas
    etapasa=['1','2','3','4']
    choicema16 = st.select_slider('Etapa atual do alinhmanto:', options=etapasa)
    #st.write("A etapa é: ",choicem)
    mz2[0,0]='16'
    mz2[0,6]=choicema16
    if choicema16 == '1':
        mz2[0,1]=1
        mz2[0,7]=161
    if choicema16 == '2':
        mz2[0,2]=1
        mz2[0,7]=162
    if choicema16 == '3':
        mz2[0,3]=1 
        mz2[0,7]=163
    if choicema16 == '4':
        mz2[0,4]=1
        mz2[0,7]=164
    np.save(file = 'TEA16', arr=mz2) 
    #.....fim etapas


if choice2 == 'TEA 17 – Combinar sistemas diversos':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE17R0.png", caption="Figura 1 - TE 17", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de alinhamento", width=700)
    #...selecionar etapas
    etapasa=['1','2','3','4']
    choicem17 = st.select_slider('Etapa atual do alinhmanto:', options=etapasa)
    #st.write("A etapa é: ",choicem)
    mz2[0,0]='17'
    mz2[0,6]=choicem17
    if choicem17 == '1':
        mz2[0,1]=1
        mz2[0,7]=171
    if choicem17 == '2':
        mz2[0,2]=1
        mz2[0,7]=172
    if choicem17 == '3':
        mz2[0,3]=1 
        mz2[0,7]=173
    if choicem17 == '4':
        mz2[0,4]=1
        mz2[0,7]=174
    np.save(file = 'TEA17', arr=mz2) 
    #.....fim etapas



if choice2 == 'TEA 18 – Combinar sistemas diferentes':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE18R0.png", caption="Figura 1 - TE 18", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.gif", caption="Figura 2 - Diretrizes de alinhamento", width=700)
    #...selecionar etapas
    etapasa=['1','2','3','4']
    choicem18 = st.select_slider('Etapa atual do alinhmanto:', options=etapasa)
    #st.write("A etapa é: ",choicem)
    mz2[0,0]='18'
    mz2[0,6]=choicem18
    if choicem18 == '1':
        mz2[0,1]=1
        mz2[0,7]=181
    if choicem18 == '2':
        mz2[0,2]=1
        mz2[0,7]=182
    if choicem18 == '3':
        mz2[0,3]=1 
        mz2[0,7]=183
    if choicem18 == '4':
        mz2[0,4]=1
        mz2[0,7]=184
    np.save(file = 'TEA18', arr=mz2) 
    #.....fim etapas


#...

#.................................3.........................................................
#.......................diretrizes de orientacao...........................................
choice3 = st.selectbox('Para diretrizes de orientacao e simetria escolha a TE asociada',[' ','TES Simetria','TES Casamento com não-linearidades externas','TES Aumento do uso da cor']) 
if choice3 == 'TES Simetria':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE8R0.png", caption="Figura 1 - TE 12", width=770)
    with cols[2]:
        st.image("DFX_simetria.gif", caption="Figura 3 - Diretrizes de simetria", width=770)
    #...selecionar etapas
    etapass=['1','2','3']
    choicems8 = st.select_slider('Etapa atual da simetria:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz3[0,0]='8'
    mz3[0,6]=choicems8
    if choicems8 == '1':
        mz3[0,1]=1
        mz3[0,7]=81
    if choicems8 == '2':
        mz3[0,2]=1
        mz3[0,7]=82
    if choicems8 == '3':
        mz3[0,3]=1 
        mz3[0,7]=83
    np.save(file = 'TES8', arr=mz3) 
    #.....fim etapas

if choice3 == 'TES Casamento com não-linearidades externas':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE15R0.png", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_simetria.gif", caption="Figura 3 - Diretrizes de simetria", width=770)
    #...selecionar etapas
    etapass=['1','2','3']
    choicems15 = st.select_slider('Etapa atual da simetria:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz3[0,0]='15'
    mz3[0,6]=choicems15
    if choicems15 == '1':
        mz3[0,1]=1
        mz3[0,7]=151
    if choicems15 == '2':
        mz3[0,2]=1
        mz3[0,7]=152
    if choicems15 == '3':
        mz3[0,3]=1 
        mz3[0,7]=153
    np.save(file = 'TES15', arr=mz3) 
    #.....fim etapas

#TES Aumento do uso da cor
if choice3 == 'TES Aumento do uso da cor':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE21R0.png", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_simetria.gif", caption="Figura 3 - Diretrizes de simetria", width=770)
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems21 = st.select_slider('Etapa atual da simetria:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz3[0,0]='21'
    mz3[0,6]=choicems21
    if choicems21 == '1':
        mz3[0,1]=1
        mz3[0,7]=211
    if choicems21 == '2':
        mz3[0,2]=1
        mz3[0,7]=212
    if choicems21 == '3':
        mz3[0,3]=1 
        mz3[0,7]=213
    if choicems21 == '4':
        mz3[0,4]=1
        mz3[0,7]=214
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
    st.image("TE10R0.png", caption="Figura 1 - TE 10", width=700)
    st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=700)
if choice1 == 'TP 11 Evolução geométrica volumétrica':
    st.write("Descrição:.... "
             "Aumenta:....") 
    st.image("TE11R0.png", caption="Figura 1 - TE 11", width=700)
    st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=700)
if choice1 == 'TP 12 Dinamização':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    st.image("TE12R0.png", caption="Figura 1 - TE 12", width=700)
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
matriz1 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetorte10, vetorte11, vetorte12, vetorte13, Vz, Vz, vetorte16, vetorte17,vetorte18,Vz,Vz,Vz])
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
matriz2 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz, vetortea15, vetortea16, vetortea17,vetortea18,Vz,Vz,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
vala=matriz2[:,6]

#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]

vetortes8 = np.load(file = 'TES8.npy')
vetortes15 = np.load(file = 'TES15.npy')
vetortes21 = np.load(file = 'TES21.npy')
matriz3 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetortes8,Vz,Vz,Vz, Vz, Vz, Vz, vetortes15, Vz, Vz,Vz,Vz,Vz,vetortes21])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
vals=matriz3[:,6]

#.....................Grafico de radar
st.title("Gráfico radar do potencial evolucionário")
#...graf radar
df = pd.DataFrame({
    'Eje': ['Mat. inteligentes','Seg. espaço ','S. superfície','S. objeto','Macro/nano','Redes e fibras','Densidade','Assimetria','Linhas divisórias','E. geometria linear', 'E. geométrica volumétrica', 'Dinamizar','Coor. ações', 'ritmo','Não-linearidades externas', 'Comb. sistemas similares', 'Comb. sistemas diversos','Comb. sistemas diferentes ','19','20','cor'],
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

#    st.write("Potencial evolucionario TE12") 
    if matriz1[11,7] == 121:
        st.image("TE12R1.png", width=1000)
    if matriz1[11,7] == 122:
        st.image("TE12R2.png", width=1000)
    if matriz1[11,7] == 123:
        st.image("TE12R3.png", width=1000)
    if matriz1[11,7] == 124:
        st.image("TE12R4.png", width=1000)

#    st.write("Potencial evolucionario TE16") 
    if matriz1[15,7] == 161:
        st.image("TE16R1.png", width=1000)
    if matriz1[15,7] == 162:
        st.image("TE16R2.png", width=1000)
    if matriz1[15,7] == 163:
        st.image("TE16R3.png", width=1000)
    if matriz1[15,7] == 164:
        st.image("TE16R4.png", width=1000)

#    st.write("Potencial evolucionario TE17") 
    if matriz1[16,7] == 171:
        st.image("TE17R1.png", width=1000)
    if matriz1[16,7] == 172:
        st.image("TE17R2.png", width=1000)
    if matriz1[16,7] == 173:
        st.image("TE17R3.png", width=1000)
    if matriz1[16,7] == 174:
        st.image("TE17R4.png", width=1000)

#    st.write("Potencial evolucionario TE18") 
    if matriz1[17,7] == 181:
        st.image("TE18R1.png", width=1000)
    if matriz1[17,7] == 182:
        st.image("TE18R2.png", width=1000)
    if matriz1[17,7] == 183:
        st.image("TE18R3.png", width=1000)
    if matriz1[17,7] == 184:
        st.image("TE18R4.png", width=1000)

#...................................................................
#........................Alinhamento reporte........................
if choicer == 'Alinhamento':
    st.write("Potencial evolucionario.") 

#    st.write("Potencial evolucionario TE15") 
    if matriz2[14,7] == 151:
        st.image("TE15R1.png", width=1000)
    if matriz2[14,7] == 152:
        st.image("TE15R2.png", width=1000)
    if matriz2[14,7] == 153:
        st.image("TE15R3.png", width=1000)
    if matriz2[14,7] == 154:
        st.image("TE15R4.png", width=1000)

#    st.write("Potencial evolucionario TE16") 
    if matriz2[15,7] == 161:
        st.image("TE16R1.png", width=1000)
    if matriz2[15,7] == 162:
        st.image("TE16R2.png", width=1000)
    if matriz2[15,7] == 163:
        st.image("TE16R3.png", width=1000)
    if matriz2[15,7] == 164:
        st.image("TE16R4.png", width=1000)

#    st.write("Potencial evolucionario TE17") 
    if matriz2[16,7] == 171:
        st.image("TE17R1.png", width=1000)
    if matriz2[16,7] == 172:
        st.image("TE17R2.png", width=1000)
    if matriz2[16,7] == 173:
        st.image("TE17R3.png", width=1000)
    if matriz2[16,7] == 174:
        st.image("TE17R4.png", width=1000)

#    st.write("Potencial evolucionario TE18") 
    if matriz2[17,7] == 181:
        st.image("TE18R1.png", width=1000)
    if matriz2[17,7] == 182:
        st.image("TE18R2.png", width=1000)
    if matriz2[17,7] == 183:
        st.image("TE18R3.png", width=1000)
    if matriz2[17,7] == 184:
        st.image("TE18R4.png", width=1000)

#...................................................................
#........................Simetria reporte........................
if choicer == 'Simetria':
    st.write("Potencial evolucionario.") 

#    st.write("Potencial evolucionario TE8") 
    if matriz3[7,7] == 81:
        st.image("TE8R1.png", width=1000)
    if matriz3[7,7] == 82:
        st.image("TE8R2.png", width=1000)
    if matriz3[7,7] == 83:
        st.image("TE8R3.png", width=1000)
    if matriz3[7,7] == 84:
        st.image("TE8R4.png", width=1000)

#    st.write("Potencial evolucionario TE15") 
    if matriz3[14,7] == 151:
        st.image("TE15R1.png", width=1000)
    if matriz3[14,7] == 152:
        st.image("TE15R2.png", width=1000)
    if matriz3[14,7] == 153:
        st.image("TE15R3.png", width=1000)

#    st.write("Potencial evolucionario TE21") 
    if matriz3[20,7] == 211:
        st.image("TE21R1.png", width=1000)
    if matriz3[20,7] == 212:
        st.image("TE21R2.png", width=1000)
    if matriz3[20,7] == 213:
        st.image("TE21R3.png", width=1000)
    if matriz3[20,7] == 214:
        st.image("TE21R4.png", width=1000)


#.............fim reporte.................

#....plot matrizes
st.title("Matrizes Tedencias da evolucao vs. Estapas atuais")
st.write("Diretrizes de posicionamento  ",matriz1[:,(0,1,2,3,4,5,6,7)])
st.write("Diretrizes de alinhamento",matriz2[:,(0,1,2,3,4,5,6,7)])
st.write("Diretrizes de simetria",matriz3[:,(0,1,2,3,4,5,6,7)])

#streamlit run teste5.py  
#pip freeze > requirements.txt
#pip show plotly


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
mz4 = np.zeros((1,8))
mz5 = np.zeros((1,8))
mz6 = np.zeros((1,8))
mz7 = np.zeros((1,8))
mz8 = np.zeros((1,8))
#mz1[0,0]=1
#....Diretrizes de Inserção
st.title("Operações de Inserção")
#............................Posicionamento..............................
choice1 = st.selectbox('Para as diretrizes de posicionamento ',['Escolha a TE asociada','TP 10 Evolução geométrica linear','TP 11 Evolução geométrica volumétrica','TP 12 Dinamização','TP 13 – Coordenação das ações','TP 16 – Combinar sistemas similares','TP 17 – Combinar sistemas diversos','TP 18 – Combinar sistemas diferentes']) 
if choice1 == 'TP 10 Evolução geométrica linear':
    st.write("Descrição: Passar de um objeto de 1D ou 2D para 3D, de acordo com os requerimentos.")
    st.write("Aumenta: Distribuição de cargas e de fluxo, área de superfície, facilita orientação de montagem, nova função, resistência, momento de inercia, estética, ergonomia.")
    #...selecionar etapas.....
    etapas=['1','2','3','4']
    choicem10 = st.select_slider('Selecione a etapa atual:', options=etapas)
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
#....plotar figuras....
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE10R0.png", caption="Figura 1 - TE 10", width=700)
    with cols[2]:
        st.image("DFX_posicionamento.png", caption="Figura 2 - Diretrizes de posicionamento", width=500)


if choice1 == 'TP 11 Evolução geométrica volumétrica':
    st.write("**Descrição:** A geometria volumétrica pode melhorar ou adicionar caraterísticas. A evolução da tecnologia facilita esta tendencia.")
    st.write("**Aumenta:** Distribuição de cargas e de fluxo, área de superfície, facilita orientação de montagem, nova função, resistência, momento de inercia, estética, ergonomia." )
    #...selecionar etapas
    etapas=['1','2','3','4']
    choicem11 = st.select_slider('Selecione a etapa atual:', options=etapas)
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
    #st.write("**Reduz:** Número de peças ") 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE11R0.png", caption="Figura 1 - TE 11", width=700)
    with cols[2]:
        st.image("DFX_posicionamento.png", caption="Figura 2 - Diretrizes de posicionamento", width=600)


if choice1 == 'TP 12 Dinamização':
    st.write("Descrição: Elementos rígidos tronam-se mais flexíveis e dinâmicos por meio de juntas. ")
    st.write("Aumenta: Manobrabilidade, flexibilidade de posicionamento, facilidade para montagem, variabilidade." )
    st.write("Reduz: Espaço, dificuldade de alinhamento. ") 
     #...selecionar etapas
    etapas1=['1','2','3','4','5']
    choicem12 = st.select_slider('Selecione a etapa atual:', options=etapas1)
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
  #...plot fig 
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE12R0.png", caption="Figura 1 - TE 12", width=900)
    with cols[2]:
        st.image("DFX_posicionamento.png", caption="Figura 2 - Diretrizes de posicionamento", width=600)



# TE13
if choice1 == 'TP 13 – Coordenação das ações':
    st.write("Descrição: As ações desempenhadas dentro do sistema podem evoluir de não coordenada para parcialmente ou totalmente coordenada até desempenhar diferentes ações durante os intervalos.")
    st.write("Aumenta: Eficiência do sistema, resposta a mudanças externas, segurança, novas funções." )
    st.write("Reduz: Probabilidade de danos ao sistema, desgaste e tempo de vida útil.") 
     #...selecionar etapas
    etapas1=['1','2','3','4']
    choicem13 = st.select_slider('Selecione a etapa atual:', options=etapas1)
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
  #...plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE13R0.png", caption="Figura 1 - TE 13", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.png", caption="Figura 2 - Diretrizes de posicionamento", width=600)

# TE16
if choice1 == 'TP 16 – Combinar sistemas similares':
    st.write("Descrição: Objetos similares podem ser introduzidos adicionalmente para desempenhar várias funções requeridas.")
    st.write("Aumenta: Quantidade de funções, distribuir funções, melhor conveniência para o usuário." )
    st.write("Reduz: Custo por componente do sistema.") 
     #...selecionar etapas
    etapas1=['1','2','3','4']
    choicem16 = st.select_slider('Selecione a etapa atual:', options=etapas1)
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
   #...plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE16R0.png", caption="Figura 1 - TE 16", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.png", caption="Figura 2 - Diretrizes de posicionamento", width=600)


# TE17
if choice1 == 'TP 17 – Combinar sistemas diversos':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapas1=['1','2','3','4']
    choicem17 = st.select_slider('Selecione a etapa atual:', options=etapas1)
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
    #...plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE17R0.png", caption="Figura 1 - TE 16", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.png", caption="Figura 2 - Diretrizes de posicionamento", width=600)

# TE18
if choice1 == 'TP 18 – Combinar sistemas diferentes':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
     #...selecionar etapas
    etapas1=['1','2','3','4']
    choicem18 = st.select_slider('Selecione a etapa atual:', options=etapas1)
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
   #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE18R0.png", caption="Figura 1 - TE 16", width=770)
    with cols[2]:
        st.image("DFX_posicionamento.png", caption="Figura 2 - Diretrizes de posicionamento", width=600)

#...................................................................................................
#..........................Diretrizes de Alinhamento................................................
#...................................................................................................
choice2 = st.selectbox('Para diretrizes de alinhamento',['Escolha a TE asociada','TEA 15 - Casamento com não-linearidades externas','TEA 16 – Combinar sistemas similares','TEA 17 – Combinar sistemas diversos','TEA 18 – Combinar sistemas diferentes'],) 

if choice2 == 'TEA 15 - Casamento com não-linearidades externas':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapasa=['1','2','3']
    choicema15 = st.select_slider('Selecione a etapa atual:', options=etapasa)
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
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE15R0.png", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.png", caption="Figura 2 - Diretrizes de alinhamento", width=600)

if choice2 == 'TEA 16 – Combinar sistemas similares':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapasa=['1','2','3','4']
    choicema16 = st.select_slider('Selecione a etapa atual:', options=etapasa)
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
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE16R0.png", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.png", caption="Figura 2 - Diretrizes de alinhamento", width=600)


if choice2 == 'TEA 17 – Combinar sistemas diversos':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
     #...selecionar etapas
    etapasa=['1','2','3','4']
    choicem17 = st.select_slider('Selecione a etapa atual:', options=etapasa)
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
   #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE17R0.png", caption="Figura 1 - TE 17", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.png", caption="Figura 2 - Diretrizes de alinhamento", width=700)



if choice2 == 'TEA 18 – Combinar sistemas diferentes':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapasa=['1','2','3','4']
    choicem18 = st.select_slider('Selecione a etapa atual:', options=etapasa)
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
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE18R0.png", caption="Figura 1 - TE 18", width=770)
    with cols[2]:
        st.image("DFX_alinhamento.png", caption="Figura 2 - Diretrizes de alinhamento", width=700)


#...

#.................................3.........................................................
#.......................diretrizes de orientacao...........................................
choice3 = st.selectbox('Para diretrizes de orientação',['  Escolha a TE asociada  ','TES Simetria','TES Casamento com não-linearidades externas','TES Aumento do uso da cor']) 
if choice3 == 'TES Simetria':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3']
    choicems8 = st.select_slider('Selecione a etapa atual:', options=etapass)
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
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE8R0.png", caption="Figura 1 - TE 12", width=770)
    with cols[2]:
        st.image("DFX_simetria.png", caption="Figura 3 - Diretrizes de simetria", width=770)

if choice3 == 'TES Casamento com não-linearidades externas':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3']
    choicems15 = st.select_slider('Selecione a etapa atual:', options=etapass)
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
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE15R0.png", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_simetria.png", caption="Figura 3 - Diretrizes de simetria", width=770)

#TES Aumento do uso da cor
if choice3 == 'TES Aumento do uso da cor':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems21 = st.select_slider('Selecione a etapa atual:', options=etapass)
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
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE21R0.png", caption="Figura 1 - TE 15", width=770)
    with cols[2]:
        st.image("DFX_simetria.png", caption="Figura 3 - Diretrizes de simetria", width=770)

#.................................4.........................................................
#.......................diretrizes de acesso...........................................
choice3 = st.selectbox('Para diretrizes de acesso',['Escolha a TE asociada','TE5A – Evoluir de macro para nano','TE12A - Dinamizacao','TE22A – Aumento da transparência','TE27A – Eliminação de componentes']) 
if choice3 == 'TE5A – Evoluir de macro para nano':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems5 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz4[0,0]='5'
    mz4[0,6]=choicems5
    if choicems5 == '1':
        mz4[0,1]=1
        mz4[0,7]=51
    if choicems5 == '2':
        mz4[0,2]=1
        mz4[0,7]=52
    if choicems5 == '3':
        mz4[0,3]=1 
        mz4[0,7]=53
    if choicems5 == '4':
        mz4[0,3]=1 
        mz4[0,7]=54
    np.save(file = 'TEAC5', arr=mz4) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE5R0.png", caption="Figura 1 - TE 5", width=770)
    with cols[2]:
        st.image("DFX_acesso.png", caption="Figura 3 - Diretrizes de acesso", width=770)

if choice3 == 'TE12A - Dinamizacao':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems12 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz4[0,0]='12'
    mz4[0,6]=choicems12
    if choicems12 == '1':
        mz4[0,1]=1
        mz4[0,7]=121
    if choicems12 == '2':
        mz4[0,2]=1
        mz4[0,7]=122
    if choicems12 == '3':
        mz4[0,3]=1 
        mz4[0,7]=123
    if choicems12 == '4':
        mz4[0,3]=1 
        mz4[0,7]=124
    if choicems12 == '5':
        mz4[0,3]=1 
        mz4[0,7]=125
    np.save(file = 'TEAC12', arr=mz4) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE12R0.png", caption="Figura 1 - TE 12", width=900)
    with cols[2]:
        st.image("DFX_acesso.png", caption="Figura 3 - Diretrizes de acesso", width=500)


if choice3 == 'TE22A – Aumento da transparência':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems22 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz4[0,0]='22'
    mz4[0,6]=choicems22
    if choicems22 == '1':
        mz4[0,1]=1
        mz4[0,7]=221
    if choicems22 == '2':
        mz4[0,2]=1
        mz4[0,7]=222
    if choicems22 == '3':
        mz4[0,3]=1 
        mz4[0,7]=223
    if choicems22 == '4':
        mz4[0,3]=1 
        mz4[0,7]=224
    np.save(file = 'TEAC22', arr=mz4) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE22R0.png", caption="Figura 1 - TE 5", width=770)
    with cols[2]:
        st.image("DFX_acesso.png", caption="Figura 3 - Diretrizes de acesso", width=770)


if choice3 == 'TE27A – Eliminação de componentes':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems27 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz4[0,0]='27'
    mz4[0,6]=choicems27
    if choicems27 == '1':
        mz4[0,1]=1
        mz4[0,7]=271
    if choicems27 == '2':
        mz4[0,2]=1
        mz4[0,7]=272
    if choicems27 == '3':
        mz4[0,3]=1 
        mz4[0,7]=273
    if choicems27 == '4':
        mz4[0,3]=1 
        mz4[0,7]=274
    np.save(file = 'TEAC27', arr=mz4) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE5R0.png", caption="Figura 1 - TE 5", width=770)
    with cols[2]:
        st.image("DFX_acesso.png", caption="Figura 3 - Diretrizes de acesso", width=770)


#.................................5.........................................................
#.......................diretrizes de ajuste................................................
choice3 = st.selectbox('Para diretrizes de ajuste',['Escolha a TE asociada','TE11AJ – Ev. geométrica volumétrica','TE12A - Dinamizacao','TE15AJ – Casamento com não-linearidades externas']) 
if choice3 == 'TE11AJ – Ev. geométrica volumétrica':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems11 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz5[0,0]='11'
    mz5[0,6]=choicems11
    if choicems11 == '1':
        mz5[0,1]=1
        mz5[0,7]=111
    if choicems11 == '2':
        mz5[0,2]=1
        mz5[0,7]=112
    if choicems11 == '3':
        mz5[0,3]=1 
        mz5[0,7]=113
    if choicems11 == '4':
        mz5[0,3]=1 
        mz5[0,7]=114
    np.save(file = 'TE11AJ', arr=mz5) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE11R0.png", caption="Figura 1 - TE 5", width=770)
    with cols[2]:
        st.image("DFX_ajuste.png", caption="Figura 3 - Diretrizes de ajuste", width=770)

if choice3 == 'TE12A - Dinamizacao':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4','5']
    choicems12 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz5[0,0]='12'
    mz5[0,6]=choicems12
    if choicems12 == '1':
        mz5[0,1]=1
        mz5[0,7]=121
    if choicems12 == '2':
        mz5[0,2]=1
        mz5[0,7]=122
    if choicems12 == '3':
        mz5[0,3]=1 
        mz5[0,7]=123
    if choicems12 == '4':
        mz5[0,3]=1 
        mz5[0,7]=124
    if choicems12 == '5':
        mz5[0,3]=1 
        mz5[0,7]=125
    np.save(file = 'TE12AJ', arr=mz5) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE12R0.png", caption="Figura 1 - TE 5", width=770)
    with cols[2]:
        st.image("DFX_ajuste.png", caption="Figura 3 - Diretrizes de ajuste", width=770)

if choice3 == 'TE15AJ – Casamento com não-linearidades externas':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3']
    choicems15 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz5[0,0]='15'
    mz5[0,6]=choicems15
    if choicems15 == '1':
        mz5[0,1]=1
        mz5[0,7]=151
    if choicems15 == '2':
        mz5[0,2]=1
        mz5[0,7]=152
    if choicems15 == '3':
        mz5[0,3]=1 
        mz5[0,7]=153
    np.save(file = 'TE15AJ', arr=mz5) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE15R0.png", caption="Figura 1 - TE 5", width=770)
    with cols[2]:
        st.image("DFX_ajuste.png", caption="Figura 3 - Diretrizes de ajuste", width=770)


#.................................6.........................................................
#.......................diretrizes de integração ...........................................
choice3 = st.selectbox('Para diretrizes de integração ',['Escolha a TE asociada','TE10I – Evolução da geometria linear','TE11I – Evolução geométrica volumétrica','TE27I – Eliminação de componentes','TE30I – Redução do número de conversões de energia']) 
if choice3 == 'TE10I – Evolução da geometria linear':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems10 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz6[0,0]='10'
    mz6[0,6]=choicems10
    if choicems10 == '1':
        mz6[0,1]=1
        mz6[0,7]=101
    if choicems10 == '2':
        mz6[0,2]=1
        mz6[0,7]=102
    if choicems10 == '3':
        mz6[0,3]=1 
        mz6[0,7]=103
    if choicems10 == '4':
        mz6[0,3]=1 
        mz6[0,7]=104
    np.save(file = 'TE10IN', arr=mz6) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE10R0.png", caption="Figura 1 - TE 5", width=770)
    with cols[2]:
        st.image("DFX_integracao.png", caption="Figura 3 - Diretrizes de integracao", width=770)

if choice3 == 'TE11I – Evolução geométrica volumétrica':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems11 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz6[0,0]='11'
    mz6[0,6]=choicems11
    if choicems11 == '1':
        mz6[0,1]=1
        mz6[0,7]=111
    if choicems11 == '2':
        mz6[0,2]=1
        mz6[0,7]=112
    if choicems11 == '3':
        mz6[0,3]=1 
        mz6[0,7]=113
    if choicems11 == '4':
        mz6[0,3]=1 
        mz6[0,7]=114
    np.save(file = 'TE11IN', arr=mz6) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE11R0.png", caption="Figura 1 - TE 11", width=770)
    with cols[2]:
        st.image("DFX_integracao.png", caption="Figura 3 - Diretrizes de integracao", width=770)


if choice3 == 'TE27I – Eliminação de componentes':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems27 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz6[0,0]='27'
    mz6[0,6]=choicems27
    if choicems27 == '1':
        mz6[0,1]=1
        mz6[0,7]=271
    if choicems27 == '2':
        mz6[0,2]=1
        mz6[0,7]=272
    if choicems27 == '3':
        mz6[0,3]=1 
        mz6[0,7]=273
    if choicems27 == '4':
        mz6[0,3]=1 
        mz6[0,7]=274
    np.save(file = 'TE27IN', arr=mz6) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE27R0.png", caption="Figura 1 - TE 27", width=770)
    with cols[2]:
        st.image("DFX_integracao.png", caption="Figura 3 - Diretrizes de integracao", width=770)


if choice3 == 'TE30I – Redução do número de conversões de energia':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems31 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz6[0,0]='31'
    mz6[0,6]=choicems31
    if choicems31 == '1':
        mz6[0,1]=1
        mz6[0,7]=311
    if choicems31 == '2':
        mz6[0,2]=1
        mz6[0,7]=312
    if choicems31 == '3':
        mz6[0,3]=1 
        mz6[0,7]=313
    if choicems31 == '4':
        mz6[0,3]=1 
        mz6[0,7]=314
    np.save(file = 'TE31IN', arr=mz6) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE31R0.png", caption="Figura 1 - TE 31", width=770)
    with cols[2]:
        st.image("DFX_integracao.png", caption="Figura 3 - Diretrizes de integracao", width=770)



#.................................7.........................................................
#.......................diretrizes de padronização...........................................
choice3 = st.selectbox('Para diretrizes de padronização',['Escolha a TE asociada','TE23P – Foco de compra dos clientes','']) 
if choice3 == 'TE23P – Foco de compra dos clientes':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems23 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz7[0,0]='23'
    mz7[0,6]=choicems23
    if choicems23 == '1':
        mz7[0,1]=1
        mz7[0,7]=231
    if choicems23 == '2':
        mz7[0,2]=1
        mz7[0,7]=232
    if choicems23 == '3':
        mz7[0,3]=1 
        mz7[0,7]=233
    if choicems23 == '4':
        mz7[0,3]=1 
        mz7[0,7]=234
    np.save(file = 'TE23PA', arr=mz7) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE23R0.png", caption="Figura 1 - TE 23", width=700)
    with cols[2]:
        st.image("DFX_padronizacao.png", caption="Figura 3 - Diretrizes de padronizacao", width=400)


#.................................8.........................................................
#.......................diretrizes de sequencia...........................................
choice3 = st.selectbox('Para diretrizes de sequencia',['Escolha a TE asociada','TE13SE – Coordenação das ações','TE16SE – Combinar sistemas similares','TE17SE – Combinar sistemas diversos','TE18SE – Combinar sistemas diferentes','TE26SE – Graus de liberdade']) 
if choice3 == 'TE13SE – Coordenação das ações':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems13 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz8[0,0]='13'
    mz8[0,6]=choicems13
    if choicems13 == '1':
        mz8[0,1]=1
        mz8[0,7]=131
    if choicems13 == '2':
        mz8[0,2]=1
        mz8[0,7]=132
    if choicems13 == '3':
        mz8[0,3]=1 
        mz8[0,7]=133
    if choicems13 == '4':
        mz8[0,3]=1 
        mz8[0,7]=134
    np.save(file = 'TE13SE', arr=mz8) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE13R0.png", caption="Figura 1 - TE 13", width=770)
    with cols[2]:
        st.image("DFX_sequencia.png", caption="Figura 3 - Diretrizes de sequencia", width=440)


if choice3 == 'TE16SE – Combinar sistemas similares':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems16 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz8[0,0]='16'
    mz8[0,6]=choicems16
    if choicems16 == '1':
        mz8[0,1]=1
        mz8[0,7]=161
    if choicems16 == '2':
        mz8[0,2]=1
        mz8[0,7]=162
    if choicems16 == '3':
        mz8[0,3]=1 
        mz8[0,7]=163
    if choicems16 == '4':
        mz8[0,3]=1 
        mz8[0,7]=164
    np.save(file = 'TE16SE', arr=mz8) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE16R0.png", caption="Figura 1 - TE 13", width=770)
    with cols[2]:
        st.image("DFX_sequencia.png", caption="Figura 3 - Diretrizes de sequencia", width=440)

if choice3 == 'TE17SE – Combinar sistemas diversos':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems17 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz8[0,0]='17'
    mz8[0,6]=choicems17
    if choicems17 == '1':
        mz8[0,1]=1
        mz8[0,7]=171
    if choicems17 == '2':
        mz8[0,2]=1
        mz8[0,7]=172
    if choicems17 == '3':
        mz8[0,3]=1 
        mz8[0,7]=173
    if choicems17 == '4':
        mz8[0,3]=1 
        mz8[0,7]=174
    np.save(file = 'TE17SE', arr=mz8) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE17R0.png", caption="Figura 1 - TE 13", width=770)
    with cols[2]:
        st.image("DFX_sequencia.png", caption="Figura 3 - Diretrizes de sequencia", width=440)


if choice3 == 'TE18SE – Combinar sistemas diferentes':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems18 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz8[0,0]='18'
    mz8[0,6]=choicems18
    if choicems18 == '1':
        mz8[0,1]=1
        mz8[0,7]=181
    if choicems18 == '2':
        mz8[0,2]=1
        mz8[0,7]=182
    if choicems18 == '3':
        mz8[0,3]=1 
        mz8[0,7]=183
    if choicems18 == '4':
        mz8[0,3]=1 
        mz8[0,7]=184
    np.save(file = 'TE18SE', arr=mz8) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE18R0.png", caption="Figura 1 - TE 13", width=770)
    with cols[2]:
        st.image("DFX_sequencia.png", caption="Figura 3 - Diretrizes de sequencia", width=440)


if choice3 == 'TE26SE – Graus de liberdade':
    st.write("Descrição: ")
    st.write("Aumenta: " )
    st.write("Reduz:  ") 
    #...selecionar etapas
    etapass=['1','2','3','4']
    choicems26 = st.select_slider('Selecione a etapa atual:', options=etapass)
    #st.write("A etapa é: ",choicem)
    mz8[0,0]='26'
    mz8[0,6]=choicems26
    if choicems26 == '1':
        mz8[0,1]=1
        mz8[0,7]=261
    if choicems26 == '2':
        mz8[0,2]=1
        mz8[0,7]=262
    if choicems26 == '3':
        mz8[0,3]=1 
        mz8[0,7]=263
    if choicems26 == '4':
        mz8[0,3]=1 
        mz8[0,7]=264
    np.save(file = 'TE26SE', arr=mz8) 
    #.....fim etapas
    #plot figuras
    cols = st.columns([2, 2, 4])
    with cols[0]:
        st.image("TE26R0.png", caption="Figura 1 - TE 13", width=770)
    with cols[2]:
        st.image("DFX_sequencia.png", caption="Figura 3 - Diretrizes de sequencia", width=440)


#......................................................................................................


#............................................................................................
#...........................................MATRIZES.........................................
#etapasmatriz = ['TE / Etapas','1','2','3','4','5']
Vz = [1,1,1,1,1,1,1,1]
vetorte10 = np.load(file = 'TE10.npy')
vetorte11 = np.load(file = 'TE11.npy')
vetorte12 = np.load(file = 'TE12.npy')
vetorte13 = np.load(file = 'TE13.npy')
vetorte16 = np.load(file = 'TE16.npy')
vetorte17 = np.load(file = 'TE17.npy')
vetorte18 = np.load(file = 'TE18.npy')
matriz1 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetorte10, vetorte11, vetorte12, vetorte13, Vz, Vz, vetorte16, vetorte17,vetorte18,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
valpos=matriz1[:,6]
#st.write("Vlor de cada tendencia",val)

#...
#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]
vetortea12 = np.load(file = 'TEA12.npy')
vetortea15 = np.load(file = 'TEA15.npy')
vetortea16 = np.load(file = 'TEA16.npy')
vetortea17 = np.load(file = 'TEA17.npy')
vetortea18 = np.load(file = 'TEA18.npy')
matriz2 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz, vetortea15, vetortea16, vetortea17,vetortea18,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
valali=matriz2[:,6]

#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]

vetortes8 = np.load(file = 'TES8.npy')
vetortes15 = np.load(file = 'TES15.npy')
vetortes21 = np.load(file = 'TES21.npy')
matriz3 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetortes8,Vz,Vz,Vz, Vz, Vz, Vz, vetortes15, Vz, Vz,Vz,Vz,Vz,vetortes21,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
valori=matriz3[:,6]

#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]
vetortes5 = np.load(file = 'TEAC5.npy')
vetortes12 = np.load(file = 'TEAC12.npy')
vetortes22 = np.load(file = 'TEAC22.npy')
vetortes27 = np.load(file = 'TEAC27.npy')
matriz4 = np.vstack([Vz,Vz,Vz,Vz,vetortes5,Vz,Vz,Vz,Vz,Vz,Vz, vetortes12, Vz, Vz, Vz, Vz, Vz,Vz,Vz,Vz,Vz,vetortes22,Vz,Vz,Vz,Vz,vetortes27,Vz,Vz,Vz,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
valace=matriz4[:,6]

#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]
vetortes11 = np.load(file = 'TE11AJ.npy')
vetortes12 = np.load(file = 'TE12AJ.npy')
vetortes15 = np.load(file = 'TE15AJ.npy')
matriz5 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetortes11,vetortes12,Vz,Vz, vetortes15, Vz, Vz, Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
valaju=matriz5[:,6]


#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]
vetortes10 = np.load(file = 'TE10IN.npy')
vetortes11 = np.load(file = 'TE11IN.npy')
vetortes27 = np.load(file = 'TE27IN.npy')
vetortes31 = np.load(file = 'TE31IN.npy')
matriz6 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetortes10,vetortes11,Vz,Vz,Vz, Vz, Vz, Vz, Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetortes27,Vz,Vz,Vz,vetortes31])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
valint=matriz6[:,6]


#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]
vetortes23 = np.load(file = 'TE23PA.npy')
#vetortes11 = np.load(file = 'TE11IN.npy')
matriz7 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz, Vz, Vz, Vz, Vz,Vz,Vz,Vz,Vz,vetortes23,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
valpad=matriz7[:,6]

#Vzero = np.zeros((1,7))
Vz = [1,1,1,1,1,1,1,1]
vetortes13 = np.load(file = 'TE13SE.npy')
vetortes16 = np.load(file = 'TE16SE.npy')
vetortes17 = np.load(file = 'TE17SE.npy')
vetortes18 = np.load(file = 'TE18SE.npy')
vetortes26 = np.load(file = 'TE26SE.npy')
matriz8 = np.vstack([Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetortes13,Vz, Vz, vetortes16, vetortes17, vetortes18,Vz,Vz,Vz,Vz,Vz,Vz,Vz,vetortes26,Vz,Vz,Vz,Vz,Vz])
#st.write("Matriz de Tedencias vs. Estapas",matriz[:,(0,1,2,3,4,5)])
valseq=matriz8[:,6]


#.....................Grafico de radar
st.title("Gráfico radar do potencial evolucionário")
#...graf radar
df = pd.DataFrame({
    'Eje': ['1 Mat. inteligentes','2 Seg. espaço ','3 S. superfície','4 S. objeto','5 Macro/nano','6 Redes e fibras','7 Densidade','8 Assimetria','9 Linhas divisórias','10 E. geometria linear', '11 E. geométrica volumétrica', '12 Dinamização','13 Coor. ações', '14 Coor. ritmos','15 Não-linearidades externas', '16 Comb. sistemas similares', '17 Comb. sistemas diversos','18 Comb. sistemas diferentes ','19 Atenuação reduzida','20 ...','21 Uso da cor','22 Transparência','23 Foco de compra','24 ...','25 Ponto de projeto','26 Graus de liberdade','27 Eliminação de componentes','28 Controlabilidade','29 envolvimento humano','30 ...','31 conversões de energia'],
    'Valor 1': valpos,
    'Valor 2': valali,
    'Valor 3': valori,
    'Valor 4': valace,
    'Valor 5': valaju,
    'Valor 6': valint,
    'Valor 7': valpad,
    'Valor 8': valseq,
    #'Valor 2': [4, 0, 3, 4, 5]
})

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
        r=df['Valor 1'],
        theta=df['Eje'],
        fill='toself',
        name='Posicionamento'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 2'],
        theta=df['Eje'],
        fill='toself',
        name='Alinhamento'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 3'],
        theta=df['Eje'],
        fill='toself',
        name='Simetria'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 4'],
        theta=df['Eje'],
        fill='toself',
        name='Acesso'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 5'],
        theta=df['Eje'],
        fill='toself',
        name='Sequencia'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 6'],
        theta=df['Eje'],
        fill='toself',
        name='Sequencia'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 7'],
        theta=df['Eje'],
        fill='toself',
        name='Sequencia'
    ))
fig.add_trace(go.Scatterpolar(
        r=df['Valor 8'],
        theta=df['Eje'],
        fill='toself',
        name='Sequencia'
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
#st.write(mz1)


choicer = st.selectbox('Diretrizes para gerar reporte',['Escolha o grupo de diretrizes','Posicionamento','Alinhamento','Simetria','Acesso','Ajuste','Integração','Padronização','Sequencia']) 

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

#...................................................................
#...........................Acesso reporte..........................
if choicer == 'Acesso':
    st.write("Potencial evolucionario acesso") 

#    st.write("Potencial evolucionario TE5") 
    if matriz4[4,7] == 51:
        st.image("TE5R1.png", width=1000)
    if matriz4[4,7] == 52:
        st.image("TE5R2.png", width=1000)
    if matriz4[4,7] == 53:
        st.image("TE5R3.png", width=1000)
    if matriz4[4,7] == 54:
        st.image("TE5R4.png", width=1000)

#    st.write("Potencial evolucionario TE12") 
    if matriz4[11,7] == 121:
        st.image("TE12R1.png", width=1000)
    if matriz4[11,7] == 122:
        st.image("TE12R2.png", width=1000)
    if matriz4[11,7] == 123:
        st.image("TE12R3.png", width=1000)
    if matriz4[11,7] == 124:
        st.image("TE12R4.png", width=1000)
    if matriz4[11,7] == 125:
        st.image("TE12R4.png", width=1000)

#    st.write("Potencial evolucionario TE22") 
    if matriz4[21,7] == 221:
        st.image("TE22R1.png", width=1000)
    if matriz4[21,7] == 222:
        st.image("TE22R2.png", width=1000)
    if matriz4[21,7] == 223:
        st.image("TE22R3.png", width=1000)
    if matriz4[21,7] == 224:
        st.image("TE22R4.png", width=1000)

    #    st.write("Potencial evolucionario TE27") 
    if matriz4[26,7] == 271:
        st.image("TE27R1.png", width=1000)
    if matriz4[26,7] == 272:
        st.image("TE27R2.png", width=1000)
    if matriz4[26,7] == 273:
        st.image("TE27R3.png", width=1000)
    if matriz4[26,7] == 274:
        st.image("TE27R4.png", width=1000)



#...................................................................
#...........................Ajuste reporte..........................
if choicer == 'Ajuste':
    st.write("Potencial evolucionario acesso") 

#    st.write("Potencial evolucionario TE11") 
    if matriz5[10,7] == 111:
        st.image("TE11R1.png", width=1000)
    if matriz5[10,7] == 112:
        st.image("TE11R2.png", width=1000)
    if matriz5[10,7] == 113:
        st.image("TE11R3.png", width=1000)
    if matriz5[10,7] == 114:
        st.image("TE11R4.png", width=1000)

#    st.write("Potencial evolucionario TE12") 
    if matriz5[11,7] == 121:
        st.image("TE12R1.png", width=1000)
    if matriz5[11,7] == 122:
        st.image("TE12R2.png", width=1000)
    if matriz5[11,7] == 123:
        st.image("TE12R3.png", width=1000)
    if matriz5[11,7] == 124:
        st.image("TE12R4.png", width=1000)
    if matriz5[11,7] == 125:
        st.image("TE12R4.png", width=1000)


#    st.write("Potencial evolucionario TE15") 
    if matriz5[14,7] == 151:
        st.image("TE15R1.png", width=1000)
    if matriz5[14,7] == 152:
        st.image("TE15R2.png", width=1000)
    if matriz5[14,7] == 153:
        st.image("TE15R3.png", width=1000)



#...................................................................
#...........................Integracao reporte..........................
if choicer == 'Integração':
    st.write("Potencial evolucionario acesso") 

#    st.write("Potencial evolucionario TE10") 
    if matriz6[9,7] == 101:
        st.image("TE10R1.png", width=1000)
    if matriz6[9,7] == 102:
        st.image("TE10R2.png", width=1000)
    if matriz6[9,7] == 103:
        st.image("TE10R3.png", width=1000)
    if matriz6[9,7] == 104:
        st.image("TE10R4.png", width=1000)
#.............fim reporte.................

#    st.write("Potencial evolucionario TE11") 
    if matriz6[10,7] == 111:
        st.image("TE11R1.png", width=1000)
    if matriz6[10,7] == 112:
        st.image("TE11R2.png", width=1000)
    if matriz6[10,7] == 113:
        st.image("TE11R3.png", width=1000)
    if matriz6[10,7] == 114:
        st.image("TE11R4.png", width=1000)
#.............fim reporte.................

#    st.write("Potencial evolucionario TE27") 
    if matriz6[26,7] == 271:
        st.image("TE27R1.png", width=1000)
    if matriz6[26,7] == 272:
        st.image("TE27R2.png", width=1000)
    if matriz6[26,7] == 273:
        st.image("TE27R3.png", width=1000)
    if matriz6[26,7] == 274:
        st.image("TE27R4.png", width=1000)
#.............fim reporte.................

#.............Potencial evolucionario TE31.......................
    if matriz6[30,7] == 311:
        st.image("TE31R1.png", width=1000)
    if matriz6[30,7] == 312:
        st.image("TE31R2.png", width=1000)
    if matriz6[30,7] == 313:
        st.image("TE31R3.png", width=1000)
    if matriz6[30,7] == 314:
        st.image("TE31R4.png", width=1000)
#.............fim reporte.................

#...................................................................
#...........................Padronizacao reporte..........................
if choicer == 'Padronização':
    st.write("Potencial evolucionario acesso") 

#    st.write("Potencial evolucionario TE23") 
    if matriz7[22,7] == 231:
        st.image("TE23R1.png", width=1000)
    if matriz7[22,7] == 232:
        st.image("TE23R2.png", width=1000)
    if matriz7[22,7] == 233:
        st.image("TE23R3.png", width=1000)
    if matriz7[22,7] == 234:
        st.image("TE23R4.png", width=1000)


#...................................................................
#...........................Sequencia  reporte..........................
if choicer == 'Sequencia':
    st.write("Potencial evolucionario acesso") 

#    st.write("Potencial evolucionario TE13") 
    if matriz8[12,7] == 131:
        st.image("TE13R1.png", width=1000)
    if matriz8[12,7] == 132:
        st.image("TE13R2.png", width=1000)
    if matriz8[12,7] == 133:
        st.image("TE13R3.png", width=1000)
    if matriz8[12,7] == 134:
        st.image("TE13R4.png", width=1000)

#    st.write("Potencial evolucionario TE16") 
    if matriz8[15,7] == 161:
        st.image("TE16R1.png", width=1000)
    if matriz8[15,7] == 162:
        st.image("TE16R2.png", width=1000)
    if matriz8[15,7] == 163:
        st.image("TE16R3.png", width=1000)
    if matriz8[15,7] == 164:
        st.image("TE16R4.png", width=1000)

#    st.write("Potencial evolucionario TE17") 
    if matriz8[16,7] == 171:
        st.image("TE17R1.png", width=1000)
    if matriz8[16,7] == 172:
        st.image("TE17R2.png", width=1000)
    if matriz8[16,7] == 173:
        st.image("TE17R3.png", width=1000)
    if matriz8[16,7] == 174:
        st.image("TE17R4.png", width=1000)

#    st.write("Potencial evolucionario TE18") 
    if matriz8[17,7] == 181:
        st.image("TE18R1.png", width=1000)
    if matriz8[17,7] == 182:
        st.image("TE18R2.png", width=1000)
    if matriz8[17,7] == 183:
        st.image("TE18R3.png", width=1000)
    if matriz8[17,7] == 184:
        st.image("TE18R4.png", width=1000)
    
#    st.write("Potencial evolucionario TE18") 
    if matriz8[25,7] == 261:
        st.image("TE26R1.png", width=1000)
    if matriz8[25,7] == 262:
        st.image("TE26R2.png", width=1000)
    if matriz8[25,7] == 263:
        st.image("TE26R3.png", width=1000)
    if matriz8[25,7] == 264:
        st.image("TE26R4.png", width=1000)

#.............fim reporte.................
#.............fim reporte.................



#....plot matrizes
#st.title("Matrizes Tedencias da evolucao vs. Estapas atuais")
#st.write("Diretrizes de posicionamento  ",matriz1[:,(0,1,2,3,4,5,6,7)])
#st.write("Diretrizes de alinhamento",matriz2[:,(0,1,2,3,4,5,6,7)])
#st.write("Diretrizes de acesso",matriz7[:,(0,1,2,3,4,5,6,7)])

#streamlit run teste5.py  
#pip freeze > requirements.txt
#pip show plotly


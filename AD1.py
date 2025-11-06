import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
#from PIL import Image

st.set_page_config(layout="wide")
#....Diretrizes de Inserção
st.title("Avaliação de desempenho")
st.write("Selecion a pontuação para cada diretriz")
V2 = [1,2,3,4,5,6,7]
V1 = np.zeros((1,7))
Vz = [0,0,0,0,0,0,0,0,0,0,0,0]

#....Objeto Base
st.image("AD3.gif", caption="Figura 2 - Objeto Base", width=1500)
choice3 = st.radio('Pontuação do objeto Base',['10 pontos','4 pontos','1 ponto']) 
if choice3 == '10 pontos':
    Vz[0]=10
if choice3 == '4 pontos':
    Vz[0]=4
if choice3 == '1 ponto':
    Vz[0]=1

#....Orientação
st.image("AD4.gif", caption="Figura 2 - Orientação", width=1500)
choice4 = st.radio('Pontuação da Orientação',['10 pontos','4 pontos','1 ponto']) 
if choice4 == '10 pontos':
    Vz[1]=10
if choice4 == '4 pontos':
    Vz[1]=4
if choice4 == '1 ponto':
    Vz[1]=1

#....Superficie
st.image("AD5.gif", caption="Figura 2 - Superficie", width=1500)
choice4 = st.radio('Pontuação da Superficie',['10 pontos','4 pontos','1 ponto']) 
if choice4 == '10 pontos':
    Vz[2]=10
if choice4 == '4 pontos':
    Vz[2]=4
if choice4 == '1 ponto':
    Vz[2]=1

#.....Posicionamento
st.image("AD1.gif", caption="Figura 1 - Integração de funções (Peças)", width=1500)
choice1 = st.radio('Pontuação da integração de funções (Peças)',['10 pontos','4 pontos','1 ponto']) 
if choice1 == '10 pontos':
    Vz[3]=10
if choice1 == '4 pontos':
    Vz[3]=4
if choice1 == '1 ponto':
    Vz[3]=1

#.....Variedade das peças
st.image("AD2.gif", caption="Figura 2 - Variedade das peças", width=1500)
choice2 = st.radio('Pontuação variedade das peças',['10 pontos','4 pontos','1 ponto']) 
if choice2 == '10 pontos':
    V1[0,2]=10
    Vz[4]=10
if choice2 == '4 pontos':
    V1[0,2]=4
    Vz[4]=4
if choice2 == '1 ponto':
    V1[0,2]=1
    Vz[4]=1

#.....ferramentas
st.image("AD6.gif", caption="Figura 1 - Ferramentas", width=1500)
choice1 = st.radio('Pontuação do uso de ferramentas',['10 pontos','4 pontos','1 ponto']) 
if choice1 == '10 pontos':
    Vz[5]=10
if choice1 == '4 pontos':
    Vz[5]=4
if choice1 == '1 ponto':
    Vz[5]=1

#.....ferramentas
st.image("AD7.gif", caption="Figura 1 - Operação de montagem em paralelo", width=1500)
choice1 = st.radio('Pontuação de operação de montagem em paralelo',['10 pontos','4 pontos','1 ponto']) 
if choice1 == '10 pontos':
    Vz[6]=10
if choice1 == '4 pontos':
    Vz[6]=4
if choice1 == '1 ponto':
    Vz[6]=1

#.....ferramentas
st.image("AD8.gif", caption="Figura 1 - modularidade", width=1500)
choice1 = st.radio('Pontuação modularidade',['10 pontos','4 pontos','1 ponto']) 
if choice1 == '10 pontos':
    Vz[7]=10
if choice1 == '4 pontos':
    Vz[7]=4
if choice1 == '1 ponto':
    Vz[7]=1


#................grafico..........................
xx=[1,2,3,4,5,6,7,8,9,10,11,12]

fig=px.bar(x=xx,y=Vz)

st.title('Grafico das pontuaçoes das diretrizes')
st.plotly_chart(fig,use_container_width=True)
#matplotlib.pyplot.show(plt, block=None)


#streamlit run AD1.py  
 



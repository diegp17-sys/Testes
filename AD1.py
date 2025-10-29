import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
#....Diretrizes de Inserção
st.title("Avaliação de desempenho")
#.....Posicionamento
st.image("AD1.gif", caption="Figura 1 - TE 10", width=700)
choice1 = st.selectbox('Integração de peças',[' ','10 pontos','4 pontos','1 ponto']) 
if choice1 == '10 pontos':
    st.write("10 pontos") 
if choice1 == '4 pontos':
    st.write("4 pontos") 

if choice1 == '1 ponto':
    st.write("1 ponto") 

#.....Alinhamento
choice1 = st.selectbox('Variedade de peças',[' ','TEA 10 Evolução geométrica linear','TEA 11 Evolução geométrica volumétrica','TEA 12 Dinamização']) 
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


#streamlit run AD1.py  
 



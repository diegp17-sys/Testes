import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
#....Diretrizes de Inserção
st.title("Diretrizes de Inserção")
#.....Posicionamento
choice1 = st.selectbox('Para diretriz de posicionamento escolha a TE asociadas',[' ','TP1','TP2','TP3']) 
if choice1 == 'TP1':
    st.write("Descricao 1.... "
             "etapas!") 
    st.image("TE1.gif", caption="figura 1 ", width=500)
    st.image("4.gif", caption="figura 1 ", width=500)
if choice1 == 'TP2':
    st.write("Descricao 2.... "
             "etapas!") 
    st.image("2.gif", caption="figura 1 ", width=500)
    st.image("4.gif", caption="figura 1 ", width=500)
if choice1 == 'TP3':
    st.write("Descricao 3.... "
             "etapas!") 
    st.image("2.gif", caption="figura 1 ", width=500)
    st.image("4.gif", caption="figura 1 ", width=500)
#.........
choice2 = st.selectbox('Para diretrizes de alinhamento escolha a TE asociada',[' ','TA1','TA2','TA3']) 
if choice2 == 'TA1':
    st.write("Descricao.... "
             "etapas!") 
    st.image("TE1.gif", caption="figura 1 ", width=500)
if choice2 == 'TA2':
    st.write("Descricao.... "
             "etapas!") 
    st.image("2.gif", caption="figura 1 ", width=500)

#...



#....Diretrizes de fixação
st.title("Diretrizes de fixação")
#.....fixação
choice1 = st.selectbox('Para diretrizes de fixação escolha a TE asociada',[' ','TT1','TT2','TT3']) 
if choice1 == 'TT1':
    st.write("Descricao 1.... "
             "etapas!") 
    st.image("TE1.gif", caption="figura 1 ", width=500)
    st.image("4.gif", caption="figura 1 ", width=500)
if choice1 == 'TT2':
    st.write("Descricao 2.... "
             "etapas!") 
    st.image("2.gif", caption="figura 1 ", width=500)
    st.image("4.gif", caption="figura 1 ", width=500)
if choice1 == 'TT3':
    st.write("Descricao 3.... "
             "etapas!") 
    st.image("2.gif", caption="figura 1 ", width=500)
    st.image("4.gif", caption="figura 1 ", width=500)
#.........

#streamlit run teste4.py  
 

#col1, col2 = st.columns([0.1,50])

#with col2:




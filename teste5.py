import streamlit as st
# from PIL import Image

st.set_page_config(layout="wide")
#....Diretrizes de Inserção
st.title("Diretrizes de Inserção")
#.....Posicionamento
choice1 = st.selectbox('Para diretrizes de posicionamento escolha a TE asociadas',[' ','TP 10 Evolução geométrica linear','TP 11 Evolução geométrica volumétrica','TP 12 Dinamização']) 
if choice1 == 'TP 10 Evolução geométrica linear':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    st.image("TE10.gif", caption="Figura 1 - TE 10", width=300)
    st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=300)
if choice1 == 'TP 11 Evolução geométrica volumétrica':
    st.write("Descrição:.... "
             "Aumenta:....") 
    st.image("TE11.gif", caption="Figura 1 - TE 11", width=300)
    st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=300)
if choice1 == 'TP 12 Dinamização':
    st.write("Descrição:.... "
            "Aumenta:..."
            "Reduz:...") 
    st.image("TE12.gif", caption="Figura 1 - TE 12", width=300)
    st.image("DFX_posicionamento.gif", caption="Figura 2 - Diretrizes de posicionamento", width=300)
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

#streamlit run teste5.py  
#pip freeze > requirements.txt



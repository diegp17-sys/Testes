import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import io

from scipy.stats import anderson
from scipy.stats import ttest_ind

#.......Aplicacao.....
# 1. Ingresando dados  (resultados avaliacao dos alunos)
grupoA = [1,2,3,4,37,16,17,8,9,10]
grupoB = [1,2,30,4,37,16,17,28,21,10]
st.write("Dados: ", grupoA)
st.write("Dados: ", grupoB)

# Teste t para amostras independentes
t_stat, p_val = ttest_ind(grupoA, grupoB)

# 3. Exibindo os resultados
st.write("t stat: ", t_stat)
st.write("p val: ",  p_val)

if p_val < 0.05:
    st.write("com nivel de significancia 5 %, há diferenca significativa, teste T")
else:
    st.write("com nivel de significancia 5 %, NAO há diferenca significativa, teste T")
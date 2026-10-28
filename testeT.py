import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import io

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from scipy.stats import anderson
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu


#streamlit run testeT.py 
# Campo de entrada de texto
#grupo1 = st.text_input("Digite os números separados por vírgula:")
#st.write("Grupo 1: ", grupo1)

#grupo2 = st.text_input("Digite os números separados por vírgula222:")
#st.write("Grupo 2: ", grupo2)


# Digitar números via entrada do usuário

#.......Aplicacao.....
# 1. Ingresando dados  (resultados avaliacao dos alunos)
#esp  1 cesar  ..... nov
grupo_nt1 = [2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2]
grupo_nc1 = [2, 1, 1, 0, 1, 1, 2, 1, 2, 0]
# esp 2 Thais ...    NOv
grupo_nt2 = [2, 2, 2, 1, 2, 1, 2, 2, 2, 4, 2, 2, 3, 2]
grupo_nc2 = [2, 1, 1, 2, 1, 2, 1, 2, 0]
#esp 3 Diego ....   NOV
grupo_nt3 = [3, 2, 2, 2, 2, 1, 2, 2, 2, 3, 2, 2, 3, 2]
grupo_nc3 = [1, 1, 1, 2, 1, 2, 1, 2, 1]

#esp 1 Cesar ... FUN
grupo_ft1 = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0]
grupo_fc1 = [0, 0, 0, 2, 0, 0, 0, 0, 1, 0]
#esp 2 thais .... FUN
grupo_ft2 = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0]
grupo_fc2 = [0, 0, 0, 0, 0, 0, 0, 1, 0]
# esp 3 Diego ... FUN
grupo_ft3 = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0]
grupo_fc3 = [1, 0, 0, 1, 0, 0, 0, 1, 0]


#montabilidade teste
#.. esp 1 ... cesar  ... teste e controle
#grupo_c = [40, 32, 28, 40, 28, 4, 40, 40, 20, 40, 36, 40, 28, 32, 36, 28, 32, 24]
#grupo_d = [28, 32, 16, 40, 36, 36, 4, 20, 32, 36, 40, 28, 0, 24, 4, 32, 36, 36, 28, 40]
#.. esp 2 .... thais
#grupo_e = [32, 36, 28, 32, 36, 28, 32, 36, 36, 32, 40, 28, 36, 28, 40, 32, 32, 28]
#grupo_f = [32, 28, 28, 40, 28, 24, 12, 36, 32, 40, 24, 40, 32, 28, 28, 16, 40, 24, 36, 40]
#.. esp 3 .... diego
#grupo_g = [36, 28, 28, 36, 32, 12, 36, 36, 24, 32, 36, 36, 28, 24, 36, 32, 32, 20]
#grupo_h = [28, 32, 12, 36, 32, 32, 4, 24, 36, 28, 28, 32, 20, 28, 8, 20, 36, 32, 28, 40]

#... manufaturabilidade
# ... esp 1 .... cesar


st.write("Dados: ", grupo_nt1)
st.write("Dados: ", grupo_nt1)



st.write("Estatística de anderson Darling:")
####

def anderson_pvalue(stat):
    # Aproximação baseada em tabelas de Stephens (1974)
    if stat < 0.2:
        return 1.0
    elif stat < 0.34:
        return 0.25
    elif stat < 0.6:
        return 0.15
    elif stat < 0.8:
        return 0.10
    elif stat < 1.1:
        return 0.05
    elif stat < 1.5:
        return 0.025
    elif stat < 2.0:
        return 0.01
    else:
        return 0.001

#novi
st.write("Novidade")
data = np.array(grupo_nt1)
result = anderson(data, dist='norm')
st.write("Estatística A²:", result.statistic)
st.write("Valor-p aproximado:", anderson_pvalue(result.statistic))


###
st.write("Teste T:")
# Teste t para amostras independentes
t_stat, p_val = stats.ttest_ind(grupo_nt1, grupo_nc1)

# 3. Exibindo os resultados
st.write("t stat: ", t_stat)
st.write("p val: ",  p_val)

if p_val < 0.05:
    st.write("com nivel de significancia 5 %, há diferenca significativa, teste T")
else:
    st.write("com nivel de significancia 5 %, NAO há diferenca significativa, teste T")


# Plotar boxplot
fig, ax = plt.subplots()
#ax.boxplot([grupo_a, grupo_b, grupo_c, grupo_d, grupo_e, grupo_f], labels=['G. Teste', 'G. Controle','G. Teste', 'G. Controle','G. Teste', 'G. Controle'])
ax.boxplot([grupo_nt1, grupo_nc1, grupo_nt1, grupo_nc1], labels=['G. Teste', 'G. Controle','G. Teste', 'G. Controle'])

ax.set_title("Boxplot dos Grupos")
ax.set_ylabel("Mediana das soluções")

st.pyplot(fig)




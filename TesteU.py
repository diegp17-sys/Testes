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


#streamlit run TesteU.py 
# Campo de entrada de texto
#grupo1 = st.text_input("Digite os números separados por vírgula:")
#st.write("Grupo 1: ", grupo1)

#grupo2 = st.text_input("Digite os números separados por vírgula222:")
#st.write("Grupo 2: ", grupo2)


# Digitar números via entrada do usuário

#.......Aplicacao.....
# 1. Ingresando dados  (resultados avaliacao dos alunos)
#esp  1 cesar  ..... nov
#grupo_a = [2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2]
#grupo_b = [2, 1, 1, 0, 1, 1, 2, 1, 2, 0]
# esp 2 Thais ...    NOv
#grupo_c = [2, 2, 2, 1, 2, 1, 2, 2, 2, 4, 2, 2, 3, 2]
#grupo_d = [2, 1, 1, 2, 1, 2, 1, 2, 0]
#esp 3 Diego ....   NOV
#grupo_e = [3, 2, 2, 2, 2, 1, 2, 2, 2, 3, 2, 2, 3, 2]
#grupo_f = [1, 1, 1, 2, 1, 2, 1, 2, 1]

#esp 1 Cesar ... FUN
#grupo_a = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0]
#grupo_b = [0, 0, 0, 2, 0, 0, 0, 0, 1, 0]
#esp 2 thais .... FUN
#grupo_c = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0]
#grupo_d = [0, 0, 0, 0, 0, 0, 0, 1, 0]
# esp 3 Diego ... FUN
#grupo_e = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0]
#grupo_f = [1, 0, 0, 1, 0, 0, 0, 1, 0]

#esp 1 cesar  ..    motanbilidade
#grupo_a = [40, 40, 28, 24, 40, 16, 40, 40, 40, 36, 40, 40, 40, 40]
#grupo_b = [20, 32, 16, 40, 20, 24, 16, 32, 40, 24]
#esp 2 thais ..... montabilidade
#grupo_c = [40, 40, 28, 32, 40, 20, 40, 40, 40, 36, 40, 40, 40, 40]
#grupo_d = [28, 32, 20, 40, 24, 12, 36, 36, 24]
#esp 3 diego.....   montabilidade
#grupo_e = [40, 40, 40, 32, 40, 20, 40, 36, 40, 28, 36, 40, 36, 36]
#grupo_f = [12, 32, 12, 40, 12, 12, 36, 36, 20]

#esp 2 Thais ... MANUF
#grupo_c = [28, 32, 16, 28, 28, 40, 28, 28, 28, 16, 36, 32, 24, 24]
#grupo_d = [12, 28, 20, 12, 20, 16, 20, 28, 28, 20]
#esp 2 Thais ... MANUF
#grupo_c = [32, 36, 16, 28, 32, 32, 32, 36, 32, 16, 40, 36, 36, 36]
#grupo_d = [12, 28, 20, 12, 20, 20, 32, 24, 28]
#esp 3 Diego ... MANUF
#grupo_e = [32, 36, 32, 28, 32, 28, 32, 28, 32, 20, 28, 36, 32, 32]
#grupo_f = [16, 32, 20, 16, 20, 20, 28, 24, 24]


grupo_c = [32, 36, 32, 36, 28, 28, 24, 36, 36, 32, 36, 28, 28, 24, 36, 32, 36, 20]
grupo_d = [28, 36, 24, 32, 36, 32, 20, 28, 32, 28, 32, 28, 20, 20, 16, 36, 28, 32, 32, 28]
grupo_e = []
grupo_f = []

st.write("Dados: ", grupo_c)
st.write("Dados: ", grupo_d)




####
resultado = anderson(grupo_c)

print("Estatística do teste:", resultado.statistic)
print("Valores críticos:", resultado.critical_values)
print("Níveis de significância:", resultado.significance_level)

# Interpretação
for cv, sl in zip(resultado.critical_values, resultado.significance_level):
    if resultado.statistic < cv:
        st.write(f"A {sl}% de significância: os dados parecem seguir uma distribuição normal.")
    else:
        st.write(f"A {sl}% de significância: os dados NÃO seguem uma distribuição normal.")

#####


# Teste t para amostras independentes
stat_u, p_valu = mannwhitneyu(grupo_c, grupo_d, alternative='two-sided')

# 3. Exibindo os resultados
st.write("t stat: ", stat_u)
st.write("p val: ",  p_valu)

if p_valu < 0.05:
    st.write("com nivel de significancia 5 %, há diferenca significativa, teste u")
else:
    st.write("com nivel de significancia 5 %, NAO há diferenca significativa, teste u")


# Plotar boxplot
fig, ax = plt.subplots()
#ax.boxplot([grupo_a, grupo_b, grupo_c, grupo_d, grupo_e, grupo_f], labels=['G. Teste', 'G. Controle','G. Teste', 'G. Controle','G. Teste', 'G. Controle'])
ax.boxplot([grupo_c, grupo_d, grupo_e, grupo_f], labels=['G. Teste', 'G. Controle','G. Teste', 'G. Controle'])

ax.set_title("Boxplot dos Grupos")
ax.set_ylabel("Mediana das soluções")

st.pyplot(fig)




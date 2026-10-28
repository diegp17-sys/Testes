import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import io


st.write("cargar arquivo")
arquivo = st.file_uploader("escolha o arquivo", type=["png","jpg","jpeg"])


#streamlit run imageteste1.py  


#streamlit run testeimage1.py  
#pip freeze > requirements.txt
#pip show plotly


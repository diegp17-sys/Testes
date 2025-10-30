import streamlit as st
import numpy as np
# from PIL import Image

v1 = np.array([0,1,2,3,4,5])
ma1 = np.array([v1,v1])
mz1 = np.zeros((5,4))
ma4 = np.array([[1,2],[3,4],[5,6]])
print(v1)

st.write(v1 * 100) 
st.write(v1) 
ma4[1,1]=100 
st.write(ma4)
st.write(ma4[1,1]) 
mz1[1,1]=1
st.write(mz1) 
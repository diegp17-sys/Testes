import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
#st.title("Mi aplicación en pantalla completa")

# Define button styles
styles = {
    "None": {"color": "green"},
    "Reviewed": {"color": "green"},
    "NotReviewed": {"color": "red"},
    "Error": {"color": "orange"},
}
#

placeholder = st.empty()
if st.button("Apagar imagem", styles["None"]):
        placeholder.empty() # Clears the content of the placeholder

st.title("Selecione as TEs associadas as DFMA: ")

if st.button("TE1 materiais inteligentes", type="secondary",) and st.button("TE2 materiais inteligentes", type="secondary",):
        st.write("Descrição:  ")
        image = Image.open("TE1.GIF") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)
    #else:
    #    st.write("sem apertar!") 

if st.button("TE2 Segmentação do espaço ", type="secondary"):
        #image = Image.open("2.gif") # Replace with your image path
        #placeholder.image(image, caption="My Image", use_container_width=True)
        if st.button("df1 ", type="secondary"):
                st.write("df1!") 
                image = Image.open("2.gif") # Replace with your image path
                placeholder.image(image, caption="My Image", use_container_width=True)
                
if st.button("TE3 Segmentação da superfície", type="secondary"):
        image = Image.open("3.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)

if st.button("TE4 Segmentação do objeto", type="secondary"):
        image = Image.open("3.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)

if st.button("TE5 Evolução macro-nano ", type="secondary"):
        image = Image.open("3.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)

if st.button("TE6 Redes e fibras ", type="secondary"):
        image = Image.open("3.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)

if st.button("TE7 ", type="secondary"):
        image = Image.open("3.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)

if st.button("TE8 ", type="secondary"):
        image = Image.open("3.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)

if st.button("TE9 ", type="secondary"):
        image = Image.open("3.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)

if st.button("TE10 ", type="secondary"):
        image = Image.open("3.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)





#
#with col2:

#    st.write("Column 2.")

#with col3:
#    st.write("Column 3.")

# st.button("Primary Button", type="primary")
# st.button("Secondary Button (Default)", type="secondary")
# st.button("Tertiary Button", type="tertiary")

#streamlit run teste3.py  
 

# if st.button("Say Hello", type="tertiary"):
#     st.write("Hello there!")
# else:
#     st.write("Goodbye!")


# if st.button("TEs 1", type="tertiary"):
#     st.image("1.gif", caption="figura 1 ",
#          width=100)
# else:
#     st.write("sem apertar!") 
#     st.image("1.gif", caption="figura 1 ",
#          width=100)
         


#  #image: ImageOrImageList,
#    # caption: str | list[str] | None = None,
#     #width: int | None = None,
#     use_column_width: UseColumnWith = None,
#     clamp: bool = False,
#     channels: Channels = "RGB",
#     output_format: ImageFormatOrAuto = "auto",
#     /,
#     use_container_width: bool = False
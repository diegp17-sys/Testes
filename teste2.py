import streamlit as st
from PIL import Image

col1, col2, col3 = st.columns([1, 2, 1])

st.title("Selecione a TEs: ")

placeholder = st.empty()

with col1:
     
    st.title("Selecione a TEs: ")
    if st.button("Display TEs 1 ", type="tertiary"):
        # image = Image.open("1.gif") # Replace with your image path
        # placeholder.image(image, caption="My Image", use_container_width=True)
        st.image("1.gif", caption="figura 1 ",
        width=600)
       # st.button("Display TEs 2 ", type="tertiary",disabled="True")
    else:
        st.write("sem apertar!") 
    if st.button("Display TEs 2 ", type="tertiary"):
        image = Image.open("2.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)

    if st.button("Display TEs 3 ", type="tertiary"):
        image = Image.open("3.gif") # Replace with your image path
        placeholder.image(image, caption="My Image", use_container_width=True)

    if st.button("Clear Image"):
        placeholder.empty() # Clears the content of the placeholder

with col2:

    st.write("Column 2.")

with col3:
    st.write("Column 3.")

# st.button("Primary Button", type="primary")
# st.button("Secondary Button (Default)", type="secondary")
# st.button("Tertiary Button", type="tertiary")

#streamlit run teste2.py  
 

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
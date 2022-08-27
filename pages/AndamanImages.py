import streamlit as st
from display import display_images,add_bg_img

st.set_page_config(page_title="Test Images",layout="wide")
st.markdown(f"""<!DOCTYPE html>
<html>
   <head>
      <style>
         img {{
            position: relative;
            top: 0px;
            left: 0px;
         }}
         .direction {{
            position: relative;
         }}
      </style>
   </head>
   <body>
         <div class = "direction"><img src = "https://www.tutorialspoint.com/python/images/python_data_science.jpg" alt = "Tutorial" width = "100" height = "50"></div>
   </body>
</html>""",
         unsafe_allow_html=True)


add_bg_img()
st.title('Andaman and Nicobar Island Images')

display_images('Andaman and Nicobar Islands')
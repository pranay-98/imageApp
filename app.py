import streamlit as st

st.set_page_config(
    page_title="Image Gallarey",
    layout="wide"
)
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

import streamlit as st
from display import get_data,add_bg_img
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import pandas as pd

st.set_page_config(page_title="Map",layout="wide")
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
st.title("This is a kepler.gl map in streamlit")

custom_config = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [],
      "interactionConfig": {}
    },
    "mapStyle": {
      "styleType": "satellite",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": True,
        "building": True,
        "water": True,
        "land": True
      }
    }
  }
}

def display_map():

  df,blob_client1 = get_data()
  map_1 = KeplerGl(height=500,config=custom_config)

  map_1.add_data(data=df,name="cities")

  keplergl_static(map_1,height=650,width=1250)

display_map()


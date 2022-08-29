import streamlit as st
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

connect_str = "Give Your ConnectionString Here" #Give Your ConnectionString Here
container_name ="imageaccess"
container_excel = "files"

def add_bg_img():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://swall.teahub.io/photos/small/40-402760_light-color-background-for-website.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


@st.experimental_memo
def get_blob(): 

  blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  container_client = blob_service_client.get_container_client(container=container_name)

  blob_items = container_client.list_blobs()

  return blob_items,container_client

@st.experimental_memo
def get_data():
  blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  blob_client1 = blob_service_client.get_blob_client(container=container_excel, blob='metadata.xlsx')
  get_blob_data = pd.ExcelFile(blob_client1.url, engine='openpyxl')
  df= pd.read_excel(get_blob_data, engine = 'openpyxl',sheet_name=0)
  return df,blob_client1

def display_images(name):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    blob_items,container_client = get_blob()
    df,blob_client1 = get_data()
    col = st.columns(1, gap="small")

    city_name = df['name'].loc[df["state_name"] == name].unique().tolist()
    city_choice = col[0].multiselect('Select City', city_name)


    if city_choice:
        data = df['img_name'].loc[df["name"].isin(city_choice)].tolist()
    else:
        data = df['img_name'].loc[df["state_name"] == name].tolist()

    for blob in blob_items:

        if blob.name in data:
            colu = st.columns([2,1,3], gap="small")
            blob_client = container_client.get_blob_client(blob=blob.name)

            colu[0].image(blob_client.url, caption = blob.name)

            colu[2].dataframe(data=df[df['Image_id']==blob_client.url])
            title = colu[2].text_input('Comments',key =blob_client.url )

            if colu[2].button('Save Me', key=blob.name):
                df.loc[df['Image_id'] == blob_client.url, 'Comments'] = title
                df.to_excel(writer,index=False)
                writer.save()
                blob_client1.upload_blob(output.getvalue(), overwrite=True)
                st.warning('Comments Saved')
            if (df.loc[df['Image_id'] == blob_client.url, 'Comments'].iloc[0] == df.loc[df['Image_id'] == blob_client.url, 'Comments'].iloc[0]):
                colu[2].write(df.loc[df['Image_id'] == blob_client.url, 'Comments'].iloc[0])

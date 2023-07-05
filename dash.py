import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title='Dashboard')
st.title('Welcome to Dashboard')
st.subheader('import excel file: ')
excel = st.file_uploader('Chose your file:', type='xlsx')


def read(file):
    x = pd.ExcelFile(file)
    sheetnames = x.sheet_names
    selected = st.selectbox(
        "Select a sheet",
        sheetnames
    )
    df = x.parse(selected)
    return df

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
if excel:
    df = read(excel)
    st.dataframe(df)
    
import streamlit as st 
import pandas as pd 
import plotly.express as px
import os 


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR,os.pardir)
dir_of_interest =os.path.join(PARENT_DIR,"resources")
DATA_PATH = os.path.join(dir_of_interest,"data","CARS.csv")


st.title(":red[Data Science Internship : [:blue[Assignment]]]")
st.header(" :car: Analysis of Indian Car Market :car:")
st.text("The following data set is considered for the analysis of Indian Car Market")

df=pd.read_csv(DATA_PATH)
st.dataframe(df)
Cars= st.selectbox("Select the Car Maker:",df['Make'].unique())

col1, col2 = st.columns(2)
fig_1 = px.histogram(df[df['Make']==Cars],x="Model")
col1.plotly_chart(fig_1,use_container_width=True)


fig_2 = px.box(df[df['Make']==Cars],y="Model") 
col2.plotly_chart(fig_2,use_container_width=True)
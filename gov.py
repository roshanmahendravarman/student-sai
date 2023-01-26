import streamlit as st
import pandas as pd
import numpy as np
import warnings
from pandas import read_csv
from pandas import datetime
    
st.title('**BUS ANALYSIS**')
st.markdown("**welcome**") 
st.write("""
         **I have explored how people are travelling from different stops in Adelaide Metropolitan area and the rate at which passengers on each bus route are increasing.finally created a predictive model to find the load of passengers on public Bus transport system in future..** """)
st.image("https://thumbs.dreamstime.com/z/watch-out-buses-kalakad-tamil-nadu-india-circa-streets-crowded-dominating-bus-india-s-population-more-than-32158551.jpg")


st.header('**SAMPLE DATASET**')

data = pd.read_csv("bus data analysis - Sheet1.csv");
st.table(data)

t.write("**Thank You for your wonderful time**")


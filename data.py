import streamlit as st
import pickle
import pandas as pd
import numpy as np

import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected





    #st.title('About')
    st.title('Hi, roshan here :smiley:')
    st.subheader('Hope this app was useful to you :innocent:')
   

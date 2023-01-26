
import streamlit as st
import pandas as pd
import numpy as np
import warnings
from pandas import read_csv
from pandas import datetime
    
st.title('**HEART FAILURE PREDICTION**')
st.markdown("**MANISHA WELCOME YOU TO THIS WEB APP**") 
st.write("""
         **The health care industries collect huge amounts of data that contain some hidden information, which
         is useful for making effective decisions. For providing appropriate results and making effective decisions
         on data, some advanced data mining techniques are used. In this study, an effective heart disease prediction system 
         (EHDPS) is developed using neural network for predicting the risk level of heart disease. The system uses 15 medical
         parameters such as age, sex, blood pressure, cholesterol, and obesity for prediction. The EHDPS predicts the likelihood of patients getting heart disease. It enables significant knowledge, eg, relationships between medical factors related to heart disease and patterns, to be established. We have employed the multilayer perceptron neural network with backpropagation as the training algorithm. The obtained results have illustrated that the designed diagnostic system can effectively predict the risk level of heart diseases.**
         """)
st.image("https://media.istockphoto.com/vectors/3d-realistic-vector-isolated-human-heart-anatomically-correct-heart-vector-id1148910293?k=20&m=1148910293&s=612x612&w=0&h=9jvKArN3eCFYX92LINaUgLKkFlDp3xVbIrf00W6YQ3U=")


st.header('**SAMPLE DATASET**')
column = ['age','sex']
data = pd.read_csv("
import streamlit as st
import pandas as pd
import numpy as np
import warnings
from pandas import read_csv
from pandas import datetime
    
st.title('**HEART FAILURE PREDICTION**')
st.markdown("**MANISHA WELCOME YOU TO THIS WEB APP**") 
st.write("""
         **The health care industries collect huge amounts of data that contain some hidden information, which
         is useful for making effective decisions. For providing appropriate results and making effective decisions
         on data, some advanced data mining techniques are used. In this study, an effective heart disease prediction system 
         (EHDPS) is developed using neural network for predicting the risk level of heart disease. The system uses 15 medical
         parameters such as age, sex, blood pressure, cholesterol, and obesity for prediction. The EHDPS predicts the likelihood of patients getting heart disease. It enables significant knowledge, eg, relationships between medical factors related to heart disease and patterns, to be established. We have employed the multilayer perceptron neural network with backpropagation as the training algorithm. The obtained results have illustrated that the designed diagnostic system can effectively predict the risk level of heart diseases.**
         """)
st.image("https://media.istockphoto.com/vectors/3d-realistic-vector-isolated-human-heart-anatomically-correct-heart-vector-id1148910293?k=20&m=1148910293&s=612x612&w=0&h=9jvKArN3eCFYX92LINaUgLKkFlDp3xVbIrf00W6YQ3U=")


st.header('**SAMPLE DATASET**')
column = ['age','sex']
data = pd.read_csv("heart_failure_clinical_records_dataset.csv", names = column);
st.table(data)

st.header('**DATA STUDIO**')
st.image("https://media.istockphoto.com/photos/heart-medical-exam-picture-id1306663325?b=1&k=20&m=1306663325&s=170667a&w=0&h=p4in-M2wMo9mBueTVWuYnX2lHL6BI9qsFDnGTrNhkk4=")
st.image("https://cdn-images-1.medium.com/max/1600/1*PkEl-8DBQa-xEft_tacXLQ.gif")

st.write("**Thank You for your wonderful time**")
st.write("To get the source code click on the [link]https://colab.research.google.com/drive/14YZQ2swFnimLR38cwTWnz7TezC_NOrus?usp=sharing")", names = column);
st.table(data)

st.header('**DATA STUDIO**')
st.image("https://media.istockphoto.com/photos/heart-medical-exam-picture-id1306663325?b=1&k=20&m=1306663325&s=170667a&w=0&h=p4in-M2wMo9mBueTVWuYnX2lHL6BI9qsFDnGTrNhkk4=")
st.image("https://cdn-images-1.medium.com/max/1600/1*PkEl-8DBQa-xEft_tacXLQ.gif")

st.write("**Thank You for your wonderful time**")
st.write("To get the source code click on the [link]https://colab.research.google.com/drive/14YZQ2swFnimLR38cwTWnz7TezC_NOrus?usp=sharing")

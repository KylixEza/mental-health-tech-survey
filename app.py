import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import home
import prediction

clean_df = pd.read_csv('survey_cleaned.csv')

encoded_df = pd.read_csv('survey_encoded.csv')
encoded_df = encoded_df.drop('treatment', axis=1)
encoded_df = encoded_df.iloc[0:0]
new_row = pd.Series([0] * len(encoded_df.columns), index=encoded_df.columns)
empty_df = pd.concat([encoded_df, pd.DataFrame([new_row])], ignore_index=True)

total_respondent = clean_df.shape[0]

st.title('Mental Health In Tech Survey')
st.write(f'This survey was conducted on {total_respondent} respondents')
st.markdown("<hr>", unsafe_allow_html=True)

home_page_option = 'Home'
prediction_page_option = 'Predict Your Burnout'

with st.sidebar:
    selected_page = option_menu("Main Menu", [home_page_option, prediction_page_option], 
        icons=['house', 'emoji-dizzy'], menu_icon="cast", default_index=0)

if selected_page == home_page_option:
    home.build_home_page(clean_df)
elif selected_page == prediction_page_option:
    prediction.build_prediction_page(clean_df, empty_df)
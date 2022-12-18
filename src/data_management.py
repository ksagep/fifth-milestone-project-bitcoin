import numpy as np
import pandas as pd
import streamlit as st


# Determine the database you want to use
@st.cache(supress_st_warning=True, allow_output_mutation=True)
def load_bitcoin_data():
    df = pd.read.csv("outputs/dataset/collection/Bitcoin_Price_Data.csv")
    return df
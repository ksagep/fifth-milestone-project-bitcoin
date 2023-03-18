import streamlit as st
import pandas as pd
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_housing_price_data():
    path = "inputs/datasets/raw/"
    file = "BTC_USD_Price_Prediction_Data.csv"
    df = pd.read_csv(path + file)
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_clean_data(dataset):
    if dataset=="int":
        df = pd.read_csv("outputs/datasets/collection/Bitcoin_Price_Data_int.csv")
    else:
        df = pd.read_csv("outputs/datasets/collection/Bitcoin_Price_Data.csv")
    return df

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
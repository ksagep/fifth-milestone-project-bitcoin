# Import libraries
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_study_of_differences_body():

    # load the data
    df = "/workspace/fifth-milestone-project-bitcoin/jupyter_notebooks/outputs/dataset/collection/Bitcoin_Price_Data.csv"
    
    # Code copied from Study of differences Notebook
    vars_to_study = ['Closing price (USD)', '24h open (USD)']
    
    st.write("## Study of differences")
    st.info(
        f"The client interested to understand the patterns from **differences between opening and closing prices**\n"
        f"so the client can realize or decide the most relevant variables which are correlated as best option to sell Bitcoins.")

    if st.checkbox("Correlation between opening and closing price"):
        df_eda = df.filter(vars_to_study)
        prices_differences(df_eda)
       
# Code copied from Study of differences Notebook
def prices_differences(df_eda):
    target_var = ['Closing Price (USD)','24h Open (USD)']
    
    for col in vars_to_study:
    
        if df_eda[col].dtype == 'float64':
            plot_numerical(df_eda, col, target_var)
        
        else:
            plot_categorical(df_eda, col, target_var)

# Code copied from Study of differences Notebook     
def plot_numerical(newdf, col, target_var):
    plt.figure(figsize=(6, 5))
    sns.histplot(data=df, x=col, hue=2787, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)

# Code copied from Study of differences Notebook
def plot_categorical(newdf, col, target_var):

    plt.figure(figsize=(9, 5))
    sns.regplot(x=df["Closing Price (USD)"], y=df["24h Open (USD)"])

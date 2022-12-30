import os
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def page_study_of_annual_comparison_body():

    # load the data
    df = ("/workspace/fifth-milestone-project-bitcoin/app_pages/Bitcoin_Price_Data.csv")

    # filter the dataset for comparison
    df = ("/workspace/fifth-milestone-project-bitcoin/app_pages/Bitcoin_Price_Data.csv")
    usecols=range(2,4)

    newdf = df[df['Date'].str.contains('2014-03-14|01-01|06-30|12-31|2021-10-29')]
    
    # Code copied from Study of annual comparison Notebook
    vars_to_study = ['Date', 'Closing price (USD)', '24h open (USD)']

    st.write("## Study of annual comparison")
    st.info(
        f"The client would like to know:\n"
        f"As the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.")

    # Text based on Conclusions of the Study of annual comparison
    st.info(
        f"According to the plots, when the exchange rate increases,\n"
        f"**most of the time the opening price is higher** than the closing price.\n"
        f"According to the mathemathical method, as the exchange rate rises, the difference between the opening and closing value\n"
        f"**will not be smaller** than with a lower exchange rate.\n"
        f"The exchange rate was changing rapidly and the difference between the opening and closing prices were\n"
        f"**significantly bigger from january 2018** than in the previous 4 years.\n"
        f"During the sale, more attention should be paid to the opening price than to the closing price.\n"
        f"When buying, it may be more beneficial to observe the closing price."
    )

# Code based on EDA on selected variables of Study of annual comparison Notebook

    def newdf_eda():
        newdf_eda = newdf.filter(vars_to_study)

    if st.checkbox("Annual comparison between opening and closing price"):
        annual_comparison(newdf_eda)

# Code copied from Study of annual comparison Notebook and adapted to page requirements
def annual_comparison(df_eda):
    df = ("/workspace/fifth-milestone-project-bitcoin/app_pages/Bitcoin_Price_Data.csv")
    target_var = ['Date', 'Closing Price (USD)','24h Open (USD)']
    vars_to_study = ['Date', 'Closing Price (USD)', '24h Open (USD)']
    newdf = df[df['Date'].str.contains('2014-03-14|01-01|06-30|12-31|2021-10-29')]
    newdf_eda = newdf.filter(vars_to_study)
    for col in vars_to_study:
    
        plot_categorical(newdf_eda, col, target_var)
        print()
  
# Code copied from Study of annual comparison Notebook and adapted to page requirements
def plot_categorical(newdf, col, target_var):
    df = ("/workspace/fifth-milestone-project-bitcoin/app_pages/Bitcoin_Price_Data.csv")
    newdf = df[df['Date'].str.contains('2014-03-14|01-01|06-30|12-31|2021-10-29')]
    plt.figure(figsize=(9, 5))
    sns.regplot(x=newdf["24h Open (USD)"], y=newdf["Closing Price (USD)"])
    plt.show()

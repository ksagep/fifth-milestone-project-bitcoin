import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def page_study_of_annual_comparison_body():

    # load the data
    df = "outputs/dataset/collection/Bitcoin_Price_Data.csv"

    # filter the dataset for comparison
    date_conv = df['Date'].strftime("%d/%m/%Y")
    newdf = df[df['date_conv'].str.contains('2014-03-14|01-01|06-30|12-31|2021-10-29')]
    newdf_eda = newdf.filter(vars_to_study)

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

    def df_eda():
        newdf_eda = newdf.filter(vars_to_study)

    if st.checkbox("Annual comparison between opening and closing price"):
        annual_comparison(df_eda)

# Code copied from Study of annual comparison Notebook
def annual_comparison(df_eda):
    df = (pd.read_csv("/workspace/fifth-milestone-project-bitcoin/jupyter_notebooks/outputs/dataset/collection/Bitcoin_Price_Data.csv").drop(['24h High (USD)','24h Low (USD)'], axis=1))
    target_var = ['Date', 'Closing Price (USD)','24h Open (USD)']
    vars_to_study = ['Date', 'Closing Price (USD)', '24h Open (USD)']
    newdf = df[df['Date'].str.contains('2014-03-14|01-01|06-30|12-31|2021-10-29')]
    for col in vars_to_study:
    
        plot_categorical()
        print()
    

# Code copied from Study of annual comparison Notebook     
def plot_numerical(newdf, col, target_var):
    plt.figure(figsize=(6, 5))
    sns.histplot(data=newdf, x=col, hue=2787, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)

# Code copied from Study of annual comparison Notebook
def plot_categorical(newdf, col, target_var):

    plt.figure(figsize=(9, 5))
    sns.regplot(x=newdf["Closing Price (USD)"], y=newdf["24h Open (USD)"])




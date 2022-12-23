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
    date = df.Date
    date_conv = date.strftime("%d/%m/%Y")
    newdf = df[df['date_conv'].str.contains('2014-03-14|01-01|06-30|12-31|2021-10-29')]
    newdf_eda = newdf.filter(vars_to_study)

    # Code copied from Study of differences Notebook
    vars_to_study = ['Date', 'Closing price (USD)', '24h open (USD)']

    st.write("## Study of annual comparison")
    st.info(
        f"The client would like to know:\n"
        f"As the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.")

    if st.checkbox("Annual comparison between opening and closing price"):
        annual_comparison(df_eda)

# Code copied from Study of differences Notebook
def prices_differences(df_eda):
    target_var = ['Date', 'Closing Price (USD)','24h Open (USD)']

    for col in vars_to_study:
    
        if df_eda[col].dtype == 'float64':
            plot_numerical(newdf_eda, col, target_var)
        
        else:
            plot_categorical(newdf_eda, col, target_var)

# Code copied from Study of differences Notebook     
def plot_numerical(newdf, col, target_var):
    plt.figure(figsize=(6, 5))
    sns.histplot(data=newdf, x=col, hue=2787, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)

# Code copied from Study of differences Notebook
def plot_categorical(newdf, col, target_var):

    plt.figure(figsize=(9, 5))
    sns.regplot(x=newdf["Closing Price (USD)"], y=newdf["24h Open (USD)"])




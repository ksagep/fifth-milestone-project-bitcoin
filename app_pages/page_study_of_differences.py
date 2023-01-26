# Import libraries
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as img
import math
import seaborn as sns
sns.set_style("whitegrid")
from IPython.display import Image
from IPython import display

def page_study_of_differences_body():

    # load the data
    df = ("/workspace/fifth-milestone-project-bitcoin/app_pages/Bitcoin_Price_Data_int.csv")
    
    # Code copied from Study of differences Notebook
    vars_to_study = ['Closing price (USD)', '24h open (USD)']

    st.write("## Study of differences")
    st.info(
        f"The client interested to understand the patterns from **differences between opening and closing prices**\n"
        f"so the client can realize or decide the most relevant variables which are correlated as best option to sell Bitcoins.")

# Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to each other. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

# Text based on Coclusions of "Study of differences" notebook
    st.info(
        f"The correlations and plots interpretation converge. \n"
        f"The opening prices were higher more times than closing prices, **1450 vs 1337**. \n"
        f"When the client would like to sell Bitcoin, it is necessary to monitor the development of the exchange rate continuously, \n"
        f"as well as the events taking place in the world."
    )


    image = img.imread('/workspace/fifth-milestone-project-bitcoin/assets/images/study_of_diff.jpg')
    plt.imshow(image)
    plt.show()

    display.Image('/workspace/fifth-milestone-project-bitcoin/app_pages/study_of_diff.jpg')
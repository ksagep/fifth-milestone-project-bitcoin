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

    # Code copied from Study of annual comparison Notebook
    vars_to_study = ['Date', 'Closing price (USD)', '24h open (USD)']

    st.write("## Study of annual comparison")
    st.info(
        f"The client would like to know:\n"
        f"As the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.\n\n"
        f"How will correlate the opening and closing price to each other? Which period of the day could be the best for trading?")

    # Text based on Conclusions of the Study of annual comparison
    st.info(
        f"According to the plots, when the exchange rate increases,\n"
        f"**most of the time the opening price is higher** than the closing price.\n"
        f"According to the mathemathical method, as the exchange rate rises, the difference between the opening and closing value\n"
        f"**will not be smaller** than with a lower exchange rate.\n"
        f"The exchange rate was changing rapidly and the difference between the opening and closing prices were\n"
        f"**significantly bigger from january 2018** than in the previous 4 years.\n"
        f"During the sale or buying, more attention should be paid to the opening price than to the closing price.\n"
        f"When buying, it may be more beneficial to observe the closing price."
    )

    if st.checkbox("Correlation between opening and closing price"):

        image = plt.imread('/workspace/fifth-milestone-project-bitcoin/assets/images/study_of_annual.png')
        st.image(image)

    if st.checkbox("Difference between opening and closing price"):

        image = plt.imread('/workspace/fifth-milestone-project-bitcoin/assets/images/study_of_annual_duo.png')
        st.image(image)


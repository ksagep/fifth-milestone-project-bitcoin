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
from skimage import io
from skimage.io import imread, imshow

def page_study_of_differences_body():

    # load the data
    df = ("/workspace/fifth-milestone-project-bitcoin/app_pages/Bitcoin_Price_Data_int.csv")
    
    # Code copied from Study of differences Notebook
    vars_to_study = ['Closing price (USD)', '24h open (USD)']

    st.write("## Study of differences")
    st.info(
        f"The client interested to understand the patterns from **differences between opening and closing prices**\n"
        f"so the client can realize or decide the most relevant variables which are correlated as best option to sell or buy Bitcoins on a given day.")

# Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to each other. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

# Text based on Coclusions of "Study of differences" notebook
    st.info(
        f"The correlation methodss and plots interpretation converge. \n"
        f"The opening prices were higher more times than closing prices, **1450 vs 1337**. \n"
        f"In this case, it can be said that it is better to take into account the exchange rate at the opening of the market and sell the existing Bitcoin stock accordingly in order to achieve the greatest possible profit. \n"
        f"When the client would like to sell or buy Bitcoin, it is necessary to monitor the development of the exchange rate continuously, \n"
        f"as well as the events taking place in the world."
    )

# Checkbox provide possibility to display more information for client on the screen
    if st.checkbox("Difference between opening and closing prices"):

        plt.rcParams["figure.figsize"] = [3.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        f = "https://github.com/ksagep/fifth-milestone-project-bitcoin/blob/main/assets/count.png"
        a = io.imread(f)

        plt.imshow(a)
        plt.axis('off')

        plt.show()

    st.info(
            f"The values show that I subtracted the closing prices from the opening price.\n"
            f"A negative value means that the closing price was higher than the opening price.\n"
            f"In the case of a positive value, the opening price was higher. \n"
            )

# Checkbox provide possibility to display more information for client on the screen
    if st.checkbox("Correlation between opening and closing price"):

        plt.rcParams["figure.figsize"] = [3.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        f = "https://github.com/ksagep/fifth-milestone-project-bitcoin/blob/main/assets/diff.png"
        a = io.imread(f)

        plt.imshow(a)
        plt.axis('off')

        plt.show()

# Under the image there is a short result and justification
        st.info(
            f"I chose the Closing Price and the 24h Open columns and display their values in a plot to show how they are locating to each other.\n"
            f"The deviation of the values is small, they follow the line of the linear straight line.\n"
            f"The correlation is very strongly positive between the two variables which is support by the spearman (value = 0,99) and pearson (value = 0,99) correlation methods."
        )

# Checkbox provide possibility to display more information for client on the screen
    if st.checkbox("Distribution of opening and closing values"):

        plt.rcParams["figure.figsize"] = [3.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        f = "https://github.com/ksagep/fifth-milestone-project-bitcoin/blob/main/assets/diff_duo.png"
        a = io.imread(f)

        plt.imshow(a)
        plt.axis('off')

        plt.show()

# Under the image there is a short result and justification
        st.info(
            f"The picture shows the distribution of the values of the opening and closing prices, which I chose to support the correlation between the two values.\n"
            f"The shape of the two diagrams is very similar, which supports the high correlation between the two variables.\n"
            f"There are no significant differences between the individual value groups."
        )
import os
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def page_ml_predict_exchange_rate_body():

    st.write("## ML pipeline: Predict the exchange rate of Closing price")
    st.info(
        f"The regression model has been chosen to predict the exchange rate of Closing price.\n"
        f"The requirement of R2 score is 0,75+")
        
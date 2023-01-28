import streamlit as st

def page_summary_body():

    st.write("## Short project summary")

# Terms and jargons section and the description of dataset
    st.info(
        f"*Terms and jargons of the project:*\n\n"
        f"**Exchange rate**: the value of rate between Bitcoin and USD on the given day.\n\n"
        f"**Open prices**: the value of Bitcoin in USD at market open on given day.\n\n"
        f"**Closing prices**: the value of Bitcoin in USD at market close on given day.\n\n"
        f"*Description of project dataset:*\n\n"
        f"The fileformat of dataset is csv.\n"
        f"There are no missing, duplicated or infinite data in the dataset.\n\n"
        f"The **dataset** has 2786 **rows** and represents bitcoin market data.\n"
        f"Each row represents a date between 14/Mar/2014 and 29/Oct/2021.\n\n"
        f"You can find in the dataset 7 **columns** which are as follows:\n"
        f"Serial number, Currency, Date, Closing price, Opening price, 24h High and 24h Low.\n"        
        f"The last four columns contain different information about exchange rate.\n\n"
        f"The currency is USD for every exchange rate. The format of date is YY-MM-DD.\n\n"
        f"The datatype of column are as follows:\n"
        f"Serial number - int64; currency and date are object; Closing price, Opening price, 24h High and 24h Low are float64.\n\n"
        f"The dataset includes information about:\n\n"
        f"Open and closing prices which are show how the exchange rate developed during the given day.\n"
        f"The highest and lowest exchange rate value during the given day.\n\n"
        
        )

# Client's requirements section
    st.success(
        f"The project has two business requirements:\n"
        f"- The client interested to understand the patterns from **differences between opening and closing prices**\n"
        f"  so the client can realize or decide the most relevant variables which are correlated as best option to sell or buy Bitcoins on a given day.\n\n" 
        f"- The client would like to know that **as the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.**\n"
        f"  How will correlate the opening and closing price to each other? **Which period of the day could be the best for trading, opening or closing?**")

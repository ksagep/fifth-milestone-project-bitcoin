import streamlit as st

def page_summary_body():

    st.write("## Short project summary")

# Terms and jargons section and the description of dataset
    st.info(
        f"Terms and jargons of the project:\n"
        f"**Exchange rate**: the value of rate between Bitcoin and USD on the given day.\n"
        f"**Open prices**: the value of Bitcoin in USD at market open on given day.\n"
        f"**Closing prices**: the value of Bitcoin in USD at market close on given day.\n\n""
        f"Description of project dataset:\n"
        f"The **dataset** has 2786 rows and represents bitcoin market data. "
        f"Each **row** represents a date between 14/Mar/2014 and29/Oct/2021. "
        f"Each **column** contains different information about rate of exchange.\n"
        f"The data set includes information about:\n"
        f"Open and closing prices which are show how the exchange rate developed during the given day.\n"
        f"The highest and lowest exchange rate value during the given day.\n")

# Business requirements section
    st.success(
        f"The project has two business requirements:\n"
        f"- Verify the client's assumption that the daily opening price is always lower than the closing price,\n"
        f"so it is worth selling the cryptocurrency at the end of the day.\n" 
        f"- To prove as the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.")

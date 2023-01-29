import streamlit as st

def page_project_hypothesis_and_validation_body():
    st.write( "### Project hypothesis and validation")

    st.info(
        f"1. *The opening price is lower than the closing price.*\n\n"
	    f"   **Validation**: This will be validated with a correlation study and use diagrams for visualisation. Use mathematical calculation solution for better understanding of dataset.\n\n" 
        f"2. *As the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate.*\n\n"
        f"   **Validation**: This will be validated with a correlation study. Use diagrams for visualisation. Use mathematical calculation solution for better understanding of dataset.\n\n"
    )
    # Conclusions taken from studies
    st.success(
        f"*Business requirements 1:*\n\n"
        f"The correlations and plots interpretation converge. The correlation was very strongly positive (0.99) because variables moved in the same direction.\n"
        f"The opening prices were higher more times than closing prices, **1450 vs 1337**.\n"
        f"When the client would like to sell Bitcoin, it is necessary to monitor the development of the exchange rate continuously,\n"
        f"as well as the events taking place in the world.\n\n"

        f"*Business requirements 2:*\n\n"
        f"According to the plots, when the exchange rate increases,\n"
        f"**most of the time the opening price is higher** than the closing price.\n"
        f"According to the mathemathical method, as the exchange rate rises, the difference between the opening and closing value\n"
        f"**will not be smaller** than with a lower exchange rate.\n"
        f"The exchange rate was changing rapidly and the difference between the opening and closing prices were\n"
        f"**significantly bigger from january 2018** than in the previous 4 years.\n"
        f"During the sale, more attention should be paid to the opening price than to the closing price.\n"
        f"When buying, it may be more beneficial to observe the closing price."
    )
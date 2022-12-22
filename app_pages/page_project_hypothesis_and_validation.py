import streamlit as st

def page_project_hypothesis_and_validation_body():
    st.write( "### Project hypothesis and validation")

    st.info(
        f"*Business requirements 1:*\n\n"
        f"The client interested to understand the patterns from differences between opening and closing prices\n"
        f"so the client can realize or decide the most relevant variables which are correlated as best option to sell Bitcoins.\n\n"

        f"*Business requirements 2:*\n\n"
        f"The client would like to know:\n\n"
        f"As the exchange rate rises, the difference between the opening and closing value will be smaller than with a lower exchange rate."
    )
    # Conclusions taken from studies
    st.success(
        f"*Business requirements 1:*\n\n"
        f"The correlations and plots interpretation converge.\n"
        f"The closing prices are higher than opening prices, **most of the time**.\n"
        f"When the client would like to sell Bitcoin, it is necessary to monitor the development of the exchange rate,\n"
        f"as well as the events taking place in the world.\n\n"

        f"*Business requirements 2:*\n\n"
        f"According to the results, as the exchange rate rises,\n"
        f"the difference between the opening and closing value **will not be smaller** than with a lower exchange rate.\n"
        f"When the exchange rate increases, the most of the time the opening price is higher than the closing price.\n"
        f"During the sale, more attention should be paid to the opening price than to the closing price."
    )
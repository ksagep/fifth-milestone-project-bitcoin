import streamlit as st

def page_hypothesis_body():

    st.write(## Project hypothesis and validation)

# Conclusions taken from studies
    st.success(
        f"- The correlations and plots interpretation converge.\n"
        f"- The closing prices are higher than opening prices most of the time.\n"
        f"- When the client would like to sell Bitcoin, it is necessary to monitor the development of the exchange rate,\n"
        f"  as well as the events taking place in the world."

        f"- According to the results, as the exchange rate rises,\n"
        f"  the difference between the opening and closing value **will not be smaller** than with a lower exchange rate.\n"
        f"- When the exchange rate increases, the most of the time the opening price is higher than the closing price.\n"
        f"- During the sale, more attention should be paid to the opening price than to the closing price.")

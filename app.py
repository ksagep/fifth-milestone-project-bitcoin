import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_study_of_differences import page_study_of_differences_body
from app_pages.page_study_of_annual_comparison import page_study_of_annual_comparison_body
from app_pages.page_project_hypothesis_and_validation import page_project_hypothesis_and_validation_body
from app_pages.page_ml_predict_exchange_rate import page_ml_predict_exchange_rate_body

# Create an instance of the app
app = MultiPage(app_name="Bitcoin - currency of matrix")

# Add the pages to the app
app.add_page("Short project summary", page_summary_body)
app.add_page("Study of differences", page_study_of_differences_body)
app.add_page("Study of annual comparison", page_study_of_annual_comparison_body)
app.add_page("Project hypothesis and validation", page_project_hypothesis_and_validation_body)
app.add_page("Exchange rate predictor - Bitcoin", page_ml_predict_exchange_rate_body)

# Run the app
app.run()
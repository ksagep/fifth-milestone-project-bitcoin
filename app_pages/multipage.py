import streamlit as st

# Class to generate multiple Streamlit pages
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name
# Add an icon to personalize the app
        st.set_page_config(
            page_title=self.app_name,
            page_icon="💵"
        )

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})
# Create radio buttons on the main page for the subpages
    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()
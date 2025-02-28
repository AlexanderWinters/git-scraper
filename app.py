import streamlit as st


st.set_page_config(
    page_title="Git Scraper",
    page_icon="🔖",
    #layout="wide",
    #initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/AlexanderWinters/git-scraper',
        'Report a bug': "https://github.com/AlexanderWinters/git-scraper/issues",
        'About': "A tool that reads basic info from a git repo, and puts it in a csv. Follow me on Github for more cool projects. https://github.com/AlexanderWinters"
    }
)
st.title("Git Scraper")

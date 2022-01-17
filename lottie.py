from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import streamlit as st

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


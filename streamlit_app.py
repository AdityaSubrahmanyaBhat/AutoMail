import streamlit as st
from streamlit_lottie import st_lottie
import lottie
import app
# from PIL import Image
# import base64

# file_ = open("../assets/mic.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()
# st.markdown(f"<img src='data:image/gif;base64,{data_url}' alt='mic'/>",unsafe_allow_html=True)
# st.markdown(f"<script src='https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js'></script><lottie-player src='https://assets6.lottiefiles.com/packages/lf20_kujkzll7.json'  background='transparent'  speed='1'  style='width: 300px; height: 300px;'  loop controls autoplay></lottie-player>",unsafe_allow_html=True)



lottie_url = "https://assets4.lottiefiles.com/packages/lf20_tpnlcuqv.json"

json=lottie.load_lottieurl(lottie_url)
# st_lottie(json)
# app.main()
res=False
def start():
    res=True

def main():
    st.markdown(f'<h1 style="text-align:center; padding:25px">{"AutoMail"}</h1>',unsafe_allow_html=True)
    st.title('')
    st.title('')
    st.title('')
    st.title('')

    col1,col2,col3,col4,col5=st.columns(5)
    placeholder=col3.empty()
    isclick = placeholder.button('Start service')
    if isclick:
        placeholder.empty()
        st_lottie(json)
        app.main()
            
    # res=col3.button("Start service")
    # st.markdown(f'<div style="text-align:center"><button onclick="start()" style="text-align:center;background-color:transparent;color:white;border-radius:12px; padding:15px 30px; justify-content:center;">{"Start service"}</button></div>',unsafe_allow_html=True)
        

if __name__=="__main__":
    main()
import streamlit as st
import os
from scrape_image import get_options
import time
import pywhatkit as py
import pyautogui 
from PIL import Image

with Image.open('Tap-Smart Logo-1.png') as f:
    img=f.resize((180,120))


st.image(img)

def save_file(file):
    folder = "C:/Users/chris/OneDrive/Documents/Python Projects/Prompt Generator/profiles_db"
    with open(os.path.join(folder, file.name), 'wb') as f:
        f.write(file.getbuffer())
    
    return os.path.join(folder, file.name)

def signup():
    st.title("Enter Your Friend's Information")
    with st.form("Profile Setup"):
        file = st.file_uploader("Upload Profile", type=["jpg", "png", "pdf"])
        extra = st.text_input('Additional Information You Know').strip()
        phone_no = st.text_input("Phone Number (With Country Code)").strip()
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.regist=True
            st.session_state.path=save_file(file)
            st.session_state.extra=extra
            st.session_state.phone_no=phone_no
            st.rerun()

def show_opt():
    
    def cache():
        st.session_state.confirm=True
        st.session_state.final=st.session_state.ans
            
    if 'confirm' not in st.session_state:
        st.session_state.confirm=False
    
    opt=get_options(st.session_state.path,st.session_state.extra)

    if st.session_state.confirm==False:
        
        with st.form("Prompt"):
            st.text_area("Prompt",value=opt,key='ans')
            submitted = st.form_submit_button("Submit",on_click=cache)
        st.button('Generate Another Prompt')
    else:
        send_msg()


def send_msg():
    py.sendwhatmsg_instantly(phone_no=st.session_state.phone_no, message=st.session_state.final,tab_close=False)
    # pyautogui.press('enter')
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()

    

if 'regist' not in st.session_state:
    st.session_state.regist=False

if st.session_state.regist==False:
    signup()
else:
    show_opt()
    
    







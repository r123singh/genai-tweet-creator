import streamlit as st
from utils import (init_client, 
                   generate_tweet, 
                   current_tweet)

st.title("🐦 Tweet writer")

open_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if open_api_key:
    init_client(open_api_key)

def disable(b):
    st.session_state["disabled"] = b
    

description = st.text_area("Enter description", height=250)


btn1,btn2 = st.columns(2,gap="small")

with btn1:
    submitted = st.button("Submit", key="btn_submit", on_click=disable, args=(False,), type="primary")

with btn2:    
    regenerate = st.button("Regenerate", key = "btn_regen" ,type="secondary", disabled=st.session_state.get("disabled", True))
    
if not open_api_key:
    st.info("Please input the OpenAI API Key")
       
elif submitted:
    if description:
        tweet = generate_tweet(description)
        st.write(tweet)
    
elif regenerate:
    if current_tweet!="":
        tweet = generate_tweet(current_tweet)
        st.write(tweet)


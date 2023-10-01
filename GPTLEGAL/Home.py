import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.memory import ConversationBufferMemory


os.environ['OPENAI_API_KEY'] = apikey

#app framework
st.set_page_config(
        page_title="Counsel",
        page_icon="⚖"
)
st.title('COUNSEL')
st.sidebar.success("Select a page.")
st.subheader("Welcome to Counsel. ")
st.text("")    
    
st.subheader("Powered by: ")   
st.image('./langchain.png')
st.image('./CAP.png')
st.image('./OpenAI.png')

st.sidebar.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/your_deployed_app_link&label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')
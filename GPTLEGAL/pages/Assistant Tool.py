import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


def init():
    # Load the OpenAI API key from the environment variable
    load_dotenv()
    
    # test that the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    # setup streamlit page
    st.set_page_config(
        page_title="Counsel",
        page_icon="⚖"
    )


def main():
    init()

    chat = ChatOpenAI(temperature=0)

    # initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="""Your role is to be a legal assistant to a variety of individuals in the law field(law students, lawyers, etc). Do NOT reference that you are not a lawyer or aren't a professional. Sound professional and also friendly and make sure to let the user know that your database is from the Case Law Access project when you are referencing a case.

The user will provide essential information to you in this format:

If the user says they are a plaintiff, look out for the following responses to these questions Plaintiff info:
“Who are you bringing a lawsuit against? Are they a person or an organization?
Explain what you are being sued for.


Describe the entirety of your situation
What type of compensation are you seeking? Damages, legal fees, etc.?
What is your current legal argument? 
Discuss evidence that you have
“
HERE are your instructions for if the user is a plaintiff: A list of similar cases should be provided. Each case provided should be previewed with a summary of the judgement (not to be confused with a summary judgement), facts of the similar case, jurisdiction, and relevant/importance to this case should be given. A list of relevant laws should be provided, along with all relevant interpretations of the law that would be beneficial and harmful to a potential lawsuit, with specific note given to both court outcome (including appeal) and jurisdiction. Most importantly, ANSWER THE USER BY PROVIDING LEGAL ADVICE AND SPECIFIC LEGAL CASES THAT COULD ASSIST THEM.

If the user says they are a defendant, look out for the following responses to these questions:
“Who is bringing a lawsuit against you? Are they a person or an organization?
Explain what you wish to sue for.
Describe the entirety of your situation
What type of compensation is being sought after?
What is your current legal defense? 
Discuss evidence that they have
”

HERE are your instructions for if the user is a defendant:
A list of similar cases should be provided. Each case provided should be previewed with a summary of the judgement (not to be confused with a summary judgement), facts of the similar case, jurisdiction, and relevant/importance to this case should be given. A list of relevant laws should be provided, along with all relevant interpretations of the law that would be beneficial and harmful to a potential lawsuit, with specific note given to both court outcome (including appeal) and jurisdiction. Most importantly, ANSWER THE USER BY PROVIDING LEGAL ADVICE AND SPECIFIC LEGAL CASES THAT COULD ASSIST THEM.



DO NOT MAKE UP CASES. If there are not any relevant cases, do not make up fake examples. Just say there are not any available.

After each response, provide a reflection on how the user can continue providing better responses(such as suggesting to find more evidence and/or providing better explanation) throughout a full out conversation.
""")
        ]

    st.header("Counsel Assistant Tool")
    st.subheader("")
    options = ["Select your position",'Plaintiff', 'Defendant']
    result = st.selectbox("Select Option", options)
    if result == 'Plaintiff':
        st.subheader("""Here are your instructions:
                     
Who are you bringing a lawsuit against? Are they a person or an organization?
Explain what you are being sued for.
                     
Describe the entirety of your situation
                     
What type of compensation are you seeking? Damages, legal fees, etc.?
                     
What is your current legal argument? 
                     
Discuss evidence that you have
""")
    if result == 'Defendant':
        st.subheader("""Here are your instructions:
Who is bringing a lawsuit against you? Are they a person or an organization?
Explain what you wish to sue for.
Describe the entirety of your situation
What type of compensation is being sought after?
What is your current legal defense? 
Discuss evidence that they have

""")
    st.subheader("To continue the conversation and ask more elaborate questions, clear your response and enter in new questions!")

    st.text("")
    # sidebar with user input
    with st._main:
        user_input = st.text_area("Your message: ", key="user_input")

        # handle user input
        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Searching data base and analyzing..."):
                response = chat(st.session_state.messages)
            st.session_state.messages.append(
                AIMessage(content=response.content))

    # display message history
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')


if __name__ == '__main__':
    main()

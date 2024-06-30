from gradio_client import Client
import streamlit as st 
import time

client = Client("chiragchetnani/Kapil_Project")

def answer(question) : 

    result = client.predict(
            question
    )

    return result

def check_prompt(prompt) : 

    '''
    Function to check the prompt

    Args:
    prompt : str : The prompt to be checked

    Returns:
    bool : The boolean value indicating whether the prompt is valid or not
    '''

    try : 
        prompt.replace('' , '')
        return True 
    except : return False


def check_mesaage() : 
    '''
    Function to check the messages
    '''

    if 'messages' not in st.session_state : st.session_state.messages = []

check_mesaage()

for message in st.session_state.messages : 

    with st.chat_message(message['role']) : st.markdown(message['content'])

prompt = st.chat_input('Ask me anything')

if check_prompt(prompt) :

    with st.chat_message('user'): st.markdown(prompt)

    st.session_state.messages.append({
        'role' : 'user' , 
        'content' : prompt
    })

    if prompt != None or prompt != '' : 


        start_time = time.time()
        response = answer(prompt)
        end_time = time.time()

        elapsed_time = end_time - start_time

        st.sidebar.write(elapsed_time)

        with st.chat_message('assistant') : st.markdown(response)

        st.session_state.messages.append({
            'role' : 'assistant' , 
            'content' : response
        })

import streamlit as st
from streamlit_chat import message
from bardapi import Bard


def generate_response(prompt):
    token = 'XwjsURlfq-r2R6M7xYYnVNJ5VZyWLyblVoNuEejmqGMk4Z6v9KuislrHbK9V4oQXu8vhqQ.'
    bard = Bard(token=token)
    response=bard.get_answer(prompt)['content']
    return response


def get_text():
    input_text=st.text_input("Your Message:","Hey Wassup?",key='input')
    return input_text


st.title('Luna Bot')


# data-testid="stAppViewContainer"
changes='''
<style>
    [data-testid="stAppViewContainer"]
    {
        background-image:url("https://images.unsplash.com/photo-1488415032361-b7e238421f1b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1469&q=80");
        background-size:auto;
    }
</style>
'''
if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

st.markdown(changes,unsafe_allow_html=True)
print(st.session_state)
#Accepting input
user_input=get_text()
if user_input:
    print(user_input)
    output=generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state['generated'][i],key=str(i))
        message(st.session_state['past'][i],key="user"+str(i),is_user=True)




import openai
import streamlit as st
from streamlit_chat import message
import re
import os

count = 0
openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_response(name):
    
   
    
    
    
    #Here we need a model for extracting the name of the person
    context = "Create a clever pickup line by rhyming it multiple times with the name - " + name +  "Keep it to 1 line only" + "Make sure you rhyme it with the name only"
    
    response = openai.ChatCompletion.create(
                                        model="gpt-3.5-turbo",
                                        messages=[{"role": "user", "content": context}]
                                            )
    
    message = response['choices'][0]['message']['content']
    return message

# EXECUTION OF THE PROGRAM STARTS HERE

st.title("Pickie - Tinder Pickup Line Generator")
st.info("Enter the name of the beautiful person")


# Storing the chat

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

prompt = get_text()
print("The prompt is :", prompt)

if prompt:
    output = generate_response(prompt)
    # Save the output
    st.session_state.past.append(prompt)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state['generated'][i], key = str(i))
        message(st.session_state['past'][i], is_user =True, key=str(i)+ '_user')

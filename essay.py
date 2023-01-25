import streamlit as st
import openai
openai.api_key = st.secrets['API_KEY']

st.header("Essay writing app")
st.text("Create AI Generated Essays in seconds")
st.text("Created by hrushik98 (github)")
st.text("")
st.text("")
topic = st.text_input("Enter topic:")
st.text("")
tone = st.selectbox(     'Select the tone of your essay:',
('Formal', 
'Informal',
'optimistic',
'worried',
'curious',
'friendly',
'Assertive',
'Encouraging',
'Surprised',
'Cooperative',
))
st.write('You selected:', tone)

st.text("")
st.text("")
no_of_words = st.slider(
    'Select number of words:',
    min_value = 100, max_value = 2000, step = 100)
st.write('You selected ', no_of_words, "words")
st.text("")
def ask(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.7,
        max_tokens= 2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    story = response['choices'][0]['text']
    st.write(story)
if st.button("Generate Essay"):
    prompt = f"""Write a {no_of_words} essay about {topic} in a tone of {tone}"""
    ask(prompt)

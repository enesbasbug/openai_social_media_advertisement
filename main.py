import openai
from api_key import openai_key
import streamlit as st

openai.api_key = openai_key


def ask_question():
    st.write('Example prompt: Can you write me a 100 word-length advertisement for a music releasing in this summer for whom between 20-25 years old people can be attracted')
    st.write('---')
    prompt = st.text_input("What kind of Social Media advertisement text suggestions you need? Let us know that and we will provide it with 10 example of hashtags:")

    if st.button("Submit"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions."
                },
                {
                    "role": "user",
                    "content": prompt + 'and create 10 keywords that can be usefull and display them as hashtag for social platforms in a table'
                }
            ]
        )

        answer = response.choices[0]['message']['content']

        st.write("Q:", prompt)
        st.write("A:", answer)


if __name__ == "__main__":
    ask_question()

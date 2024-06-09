import streamlit as st
import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = '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'  # Remember to set this using environment variable or secure storage

# CSS for background image and footer
page_style = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1487700160041-babef9c3cb55?q=80&w=2052&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 60px;
    background-color: rgba(0, 0, 0, 0.7);
    text-align: center;
    color: white;
    padding: 10px;
    font-size: 20px;
    line-height: 60px;  /* Vertically center the text */
    z-index: 1000;
}
</style>
'''

st.markdown(page_style, unsafe_allow_html=True)

st.title("Health and Wellness Chatbot")

query = st.text_input("Ask your health-related question:")
persona = "As a fitness and wellness coach, "

if query:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": query}
        ],
        max_tokens=150
    )
    st.write(response.choices[0].message['content'])

# Custom footer HTML
footer_html = '''
<footer>
    <p>Made by Rajan Panchal</p>
</footer>
'''

st.markdown(footer_html, unsafe_allow_html=True)

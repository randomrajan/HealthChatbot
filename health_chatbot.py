import streamlit as st
import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'sk-proj-CqgipuTQJaPJprfRwwDfT3BlbkFJyFhAnoUgB7zuA3qC4L6o'  # Remember to set this using environment variable or secure storage

# CSS for background image and footer
page_style = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/free-photo/close-up-stethoscope-blank-blue-background_23-2147874869.jpg?t=st=1719282418~exp=1719286018~hmac=4ffbf43671f0689b8197184967043543e6f5b40c7645853da463ca1ed9e662f3&w=1380");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 60px;
    background-color: transparent; /* Remove background color */
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

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if query:
    st.session_state.chat_history.append({"role": "user", "content": query})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": persona},
            *st.session_state.chat_history
        ],
        max_tokens=150
    )
    response_message = response.choices[0].message['content']
    st.session_state.chat_history.append({"role": "assistant", "content": response_message})
    st.write(response_message)

# Display chat history
if st.session_state.chat_history:
    st.write("## Chat History")
    for chat in st.session_state.chat_history:
        role = "User" if chat["role"] == "user" else "Bot"
        st.write(f"**{role}:** {chat['content']}")

# Custom footer HTML
footer_html = '''
<footer>
    <p>Made by Rajan Panchal</p>
</footer>
'''

st.markdown(footer_html, unsafe_allow_html=True)

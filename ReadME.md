# Health and Wellness Chatbot

This repository contains a simple Health and Wellness Chatbot built using Streamlit and OpenAI's GPT-3.5-turbo model. The chatbot provides fitness and wellness advice based on user queries.

## Features

- **Background Image**: The application has a fixed background image to enhance the visual appeal.
- **Chat Interface**: Users can ask health-related questions and receive responses from the chatbot.
- **Chat History**: Displays the history of the conversation within the session.
- **Custom Footer**: A custom footer is added at the bottom of the page.

## Prerequisites

- Python 3.7+
- Streamlit
- OpenAI Python Client

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/health-wellness-chatbot.git
   cd health-wellness-chatbot
Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

Set your OpenAI API key:
Replace 'your-api-key' in the code with your actual OpenAI API key. It's recommended to use environment variables or secure storage for this purpose.

## Usage
Run the Streamlit app:

streamlit run health_chatbot.py

2. Interact with the Chatbot:

Open your web browser and navigate to http://localhost:8501.
Ask your health-related questions in the input box and receive responses from the chatbot.
View the chat history displayed on the page.

## Code Overview

### CSS Styling:

Adds a background image to the app.
Styles the footer to be centered and transparent.

### Streamlit App:

Accepts user input for health-related queries.
Sends the user query and conversation history to the OpenAI API.
Displays the response from the chatbot.
Maintains and displays chat history within the session.

## Files
app.py: The main application file containing the Streamlit code and chatbot logic.
requirements.txt: A list of Python dependencies required to run the app.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Made by Rajan Panchal.
import streamlit as st
from google import genai
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# App title layout
st.title("THE MULTIVERSE of CHIT-CHATBOTS")

# Dropdown menu to select the bot personality
personality = st.selectbox("Who do you want to talk to?", [
    "Shinchan 👦",
    "Doraemon 🤖",
    "BTS Fan (Army) 💜",
    "Gossip Girl 🤫💅",
    "Virat Kohli Fan 👑",
    "Ronaldo Fan (SIUUU) ⚽",
    "Topper Student 📚"
])

# Initialize the Gemini API client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Input field for user message
user_message = st.text_input("Say something: ")

# Trigger action on clicking the SEND button
if st.button("SEND"):
    if user_message:
        # Dynamic prompt engineering based on selected personality
        ai_instructions = f"You are acting as {personality}. Respond to the message sent by the user staying completely in character: {user_message}"
        
        # Show loading spinner while fetching AI response
        with st.spinner("Connecting to the multiverse!......"):
            # Generate content using Gemini API
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )
            
            # Display success message and output response
            st.success("Message received!")
            st.write(response.text)
    else:
        # Warning if input field is empty
        st.warning("Please type a message first")
import streamlit as st

st.title("The Identity Echo Interface")
st.write("Enter your name and message below then press Transmit button")

user_name = st.text_input("Enter your name:")
user_message = st.text_input("Enter your message:")

if st.button("Transmit"):
    # Input validation: Check if user left any field empty
    if user_name == "":
        st.error("Please provide your name.")
    elif user_message == "":
        st.warning("Please type a message to transmit.")
    else:
        # Using f-string to dynamically display user inputs
        st.success(f"Transmission successful! Greetings,{user_name}. We received your message: {user_message}")

        # Simple token logic: 1 token is roughly equal to 4 characters
        total_character = len(user_message)
        token_count = total_character/4
        st.info(f"System Check: Your message will consume approximately {token_count} tokens from our context window.") 
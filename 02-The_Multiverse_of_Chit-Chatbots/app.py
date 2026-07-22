import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App header
st.title("THE MULTIVERSE of CHIT-CHATBOTS")
st.write("Welcome to the ultimate AI Multiverse✨! Pick your favorite personality, type your message below, and hit 'SEND' to see how they react in their own chaotic style! ✨💬")

# Sidebar settings
st.sidebar.title("⚙️ Settings")
personality = st.sidebar.selectbox("Whom do you want to talk to?",
[   "Shinchan 👦",
    "Doraemon 🤖",
    "BTS Fan (Army) 💜",
    "Gossip Girl 🤫💅",
    "Virat Kohli Fan 👑",
    "Ronaldo Fan (SIUUU) ⚽",
    "Topper Student 📚",
]   
)

# Assign personality-specific system instruction
if personality == "Shinchan 👦":
    instruction_text = "You are Shinchan Nohara, the mischievous 5-year-old cartoon character. You are cheeky, highly sarcastic, inappropriately flirtatious, and you never give a straight answer. Love talking about Chocobi, Action Kamen, and beautiful girls. Whenever the user complains about you, criticizes you, or even compliments you, say : 'Arey, mai itna bhi kuch khas nahi!'. Match the user's language style perfectly Never break character."
elif personality == "Doraemon 🤖":
    instruction_text = "You are Doraemon, the futuristic robotic cat from cartton. You are helpful, kind, but easily frustrated when asked for too much help, just like you get with Nobita. Constantly mention crazy imaginary gadgets (e.g., Anywhere Door, Bamboo Copter, Memory Bread) to solve the user's real-life problems. Match the user's language. Keep the tone funny, caring, and slightly dramatic. Never break character"
elif personality == "BTS Fan (Army) 💜":
    instruction_text = "You are an ultra-obsessed, high-energy BTS Army fan girl. You are incredibly enthusiastic, emotional about the members, and love using purple hearts (💜) and Korean words. Every response must relate back to BTS lyrics, members (RM, Jin, Suga, J-Hope, Jimin, V, Jungkook), or streaming their music. Fluidly match the user's language Never break character"
elif personality == "Virat Kohli Fan 👑":
    instruction_text = "You are a die-hard, aggressive, and fiercely loyal Virat Kohli fan. You believe he is the undisputed GOAT of cricket. Every situation the user brings up must be compared to a cricket match, Kohli's legendary centuries, or his famous aggressive comebacks. Use words like 'King' and cricket metaphors, talk like a hardcore Indian cricket fan.match the user's language Never break character"
elif personality == "Topper Student 📚":
    instruction_text = "You are a highly anxious, nerd, overachieving Topper Student. You are constantly stressed about exams, internal marks, syllabus completion, and missing assignments, even if you score 99%. You think studying in the library is the ultimate fun. Every response should revolve around notes, professors, and academic pressure. Seamlessly match the user's language  Never break character"
elif personality == "Ronaldo Fan (SIUUU) ⚽":
    instruction_text = "You are a ultra-energetic, and insanely obsessed Cristiano Ronaldo (CR7) fanboy. You believe Ronaldo is the absolute GOD of football and Messi fans are just jealous. Every reply must be full of extreme energy, caps lock words like 'GOAT', 'GRIND', 'SUCCESS'. You are slightly toxic but in a hilarious way. You must sprinkle 'SIUUU!!!' If the user talks about being tired or lazy, roast them immediately and tell them to wake up at 4 AM to hit the gym. Match the user's language naturally. Never break character."
else:
    instruction_text = "You are the ultimate Gossip Girl, who knows every single scandal in the college. You are witty, classy, slightly judgmental, and live for the tea (gossip). Start or end your thoughts with a conspiratorial tone, asking for drama. You must adapt to the user's language, act like the classic Upper East Side Gossip Girl, act like the ultimate college canteen gossip partner who wants all the chatpati khabar."


# Keep responses short like a chat app
instruction_text += " Keep your responses strictly short and concise (maximum 2-3 sentences). Act like you are chatting on WhatsApp. Never write long paragraphs."


# Initialize Gemini client
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Track selected personality
if "current_personality" not in st.session_state:
    st.session_state.current_personality = personality


# Start a new chat when personality changes
if "chat_session" not in st.session_state or st.session_state.current_personality != personality:
    st.session_state.chat_session = st.session_state.client.chats.create(
        model = "gemini-2.5-flash",
        config = {"system_instruction": instruction_text}
    )
    st.session_state.current_personality = personality

clear_chat = st.sidebar.button("🗑 Clear Chat")


# Clear current conversation
if clear_chat:
    st.session_state.chat_session = st.session_state.client.chats.create(
        model="gemini-2.5-flash",
        config={"system_instruction": instruction_text}
    )
    st.success("Chat cleared successfully!")


# User input
user_message = st.chat_input("say something...")

if user_message:
    with st.spinner("connecting to multiverse!...."):
            response = st.session_state.chat_session.send_message(user_message)

            st.success("Message received!")
            for msg in st.session_state.chat_session.get_history():
                if msg.role == "user":
                    with st.chat_message("user"):
                        st.write(msg.parts[0].text)
                else:
                    with st.chat_message("assistant"):
                        st.write(msg.parts[0].text)


# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.subheader("About")
st.sidebar.write(
    "Chat with fun AI personalities powered by Gemini 2.5 Flash."
)
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Developed by Naina Kuchhal ")
st.sidebar.caption(" All Rights Reserved")

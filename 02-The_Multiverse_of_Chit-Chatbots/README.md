# 🌌 The Multiverse of Chit-ChatBots

An interactive AI chatbot application built with **Streamlit** and powered by **Google Gemini 2.5 Flash**. Step into a multiverse where every chatbot has a completely different personality—from hilarious cartoon characters to passionate sports fans and dramatic gossip lovers.

---

## 🎭 Features

- 🤖 **7 Unique AI Personalities**
  - Shinchan 👦
  - Doraemon 🤖
  - BTS Fan (Army) 💜
  - Gossip Girl 🤫💅
  - Virat Kohli Fan 👑
  - Ronaldo Fan (SIUUU) ⚽
  - Topper Student 📚

- 🎯 **Dynamic Character Switching**
  - Instantly switch between personalities with a sidebar dropdown.

- 💬 **Context-Aware Conversations**
  - Each personality maintains its own conversation style using Gemini's chat session.

- 🎭 **Consistent Roleplay**
  - Carefully designed system prompts ensure every character stays in personality throughout the conversation.

- ⚡ **Real-Time Chat Experience**
  - Interactive chat interface with loading spinners and message history.

- 🗑️ **Clear Chat**
  - Reset the current conversation without restarting the application.

- 🎨 **Clean Streamlit UI**
  - Simple, responsive, and beginner-friendly interface.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Language:** Python
- **LLM:** Google Gemini 2.5 Flash
- **SDK:** Google GenAI SDK
- **Environment Variables:** python-dotenv

---

## 📂 Project Structure

```text
The-Multiverse-of-Chit-ChatBots/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── assets/ (optional)
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd The-Multiverse-of-Chit-ChatBots
```

### 2️⃣ Install Dependencies

Make sure you have Python installed, then run:

```pip install streamlit google-genai python-dotenv```


### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root and add your Gemini API key.

```env
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 💡 How It Works

1. Select an AI personality from the sidebar.
2. Type your message.
3. Gemini generates responses while following the selected character's personality.
4. Switch personalities anytime to start a brand-new conversation.
5. Use **Clear Chat** to reset the current chat session.

---

## 📸 Preview

![Demo](assets/demo.gif)

---

## 👩‍💻 Developed By

**Naina Kuchhal**

- LinkedIn: https://www.linkedin.com/in/naina-kuchhal2202/
- GitHub: https://github.com/nainakuchhal2202

---

## 📄 License

This project is open-source and available under the MIT License.
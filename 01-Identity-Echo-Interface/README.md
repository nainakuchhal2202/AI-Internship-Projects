# The Identity Echo Interface

An interactive Streamlit web application built during my AI Internship. This tool captures user input, validates it, and provides a mock token-consumption estimate.

## 🚀 Features
- **User Validation:** Checks if the name or message fields are left empty.
- **Dynamic Echo:** Uses Python f-strings to display personalized greeting messages.
- **Token Estimation:** Calculates an approximate token count based on character length (1 token ≈ 4 characters).

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** Streamlit

## 🏃 How to Run Locally

1. Navigate to this folder in your terminal.
2. Install dependencies (if not done already):
   pip install streamlit
3. Run using command:
    streamlit run app.py
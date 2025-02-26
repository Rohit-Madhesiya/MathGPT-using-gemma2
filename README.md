---
title: MathGPT Using Gemma2
emoji: 🐠
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.42.2
app_file: app.py
pinned: false
license: apache-2.0
short_description: allows users to solve mathematical problems
---

# Text to Math Problem Solver and Data Search Assistant

## Overview 📖🔍
This application is a **Text to Math Problem Solver and Data Search Assistant** powered by the **Gemma2-9B-IT** model and built using Streamlit. The app allows users to solve mathematical problems, retrieve data from Wikipedia, and handle logic-based reasoning questions using LangChain's tools and agents.

## Features ✨
- **Mathematical Problem Solver:** Solve complex math equations with step-by-step explanations.
- **Wikipedia Search Assistant:** Retrieve information on various topics directly from Wikipedia.
- **Reasoning Question Handler:** Answer logic-based queries using advanced AI reasoning.
- **Interactive Chat Interface:** Engage with the AI assistant using an easy-to-use chat-based UI.

## Deployment 🚀
This application is deployed on **Hugging Face Spaces**. You can access and interact with it using the following link:

👉 **[Deployment Link](https://huggingface.co/spaces/guptarohit20/MathGPT-using-gemma2)**

## Installation & Setup 🛠️
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rohit-Madhesiya/MathGPT-using-gemma2.git
cd MathGPT-using-gemma2
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key
- Create a `.env` file in the root directory.
- Add the following line:
```env
GROQ_API_KEY=<your_api_key>
```

## Usage 📌
Run the Streamlit application:
```bash
streamlit run app.py
```

Once the app is running:
1. Enter your **Groq API Key** in the sidebar.
2. Type a **mathematical question** or **logic-based query** in the chat.
3. Click **Find my answer** to get AI-generated responses.

## Dependencies 📋
The project requires the following Python libraries:
- `streamlit`
- `langchain`
- `langchain_groq`
- `langchain_community`
- `wikipedia`
- `python-dotenv`

## Project Structure 📂
```
├── app.py              # Main application file
├── requirements.txt    # List of dependencies
├── .env                # API key configuration (not included in repo)
└── README.md           # Project documentation
```

## Contributing 🤝
Feel free to fork the repository, submit pull requests, or report any issues.

## Author 👨‍💻
Developed by **[Rohit Gupta]**.


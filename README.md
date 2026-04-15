# iris.ai
# 🤖 IRIS - Intelligent Responsive Interface System

IRIS is a **Streamlit-based AI assistant demo** that showcases a responsive chat interface with natural language processing, animated feedback, and immersive UI design.  
It is built to demonstrate how conversational AI can be integrated into modern web apps with engaging visuals and interactive features.

---

## ✨ Features
- **Natural Language Processing (NLP)**  
  Uses NLTK for tokenization, stopword removal, and lemmatization to preprocess user input.

- **Responsive Chat Interface**  
  - User and bot messages styled with custom CSS.  
  - Thinking animation with pulsing dots to simulate AI "processing".  
  - Chat history maintained across interactions.

- **Animated Visual Feedback**  
  Integrates **Lottie animations** for dynamic sidebar visuals.

- **Customizable Settings**  
  - Adjustable response speed.  
  - Optional voice response toggle with selectable voice types.

---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) – UI framework
- [NLTK](https://www.nltk.org/) – Natural Language Toolkit for text preprocessing
- [Requests](https://docs.python-requests.org/) – API calls for animations
- [streamlit-lottie](https://github.com/andfanilo/streamlit-lottie) – Lottie animation integration
- Python standard libraries: `random`, `time`, `json`

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Priyanshu459/iris.ai.git
cd iris.ai
2. Install dependencies
pip install -r requirements.txt
📂 Project Structure
iris.ai/
│── app.py              # Main Streamlit application
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

⚙️ How It Works
User Input → Text is tokenized, cleaned, and lemmatized.

Response Generation → Simple rule-based logic generates replies (greetings, farewells, questions, etc.).

UI Rendering → Messages styled with CSS, animations displayed, and chat history updated.

Customization → Users can adjust response speed and enable voice settings.

🎨 Demo UI Highlights
Main Title & Subtitle styled with custom CSS.

Chat Bubbles for user and bot messages.

Thinking Animation with pulsing dots.

Sidebar with app info, Lottie animation, and settings.

🔮 Future Enhancements
Integration with advanced AI models (e.g., GPT-based APIs).

Persistent conversation memory.

Voice synthesis for real-time spoken responses.

Database connection for knowledge retrieval.

📜 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

👨‍💻 Author
Developed by Priyanshu  
📍 Indore, India
Passionate about AI, streaming, and workflow automation.

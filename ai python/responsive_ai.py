import streamlit as st
import random
import time
from streamlit_lottie import st_lottie
import requests
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources if not already downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Set page configuration
st.set_page_config(
    page_title="IRIS - Intelligent Responsive Interface System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load animation
@st.cache_data
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# App title and styling
st.markdown("""
<style>
    .main-title {
        font-size: 3rem !important;
        color: #4B9FE1;
        text-align: center;
        margin-bottom: 0rem;
        font-weight: 700;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #727272;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stTextInput>div>div>input {
        border-radius: 25px;
        padding: 15px;
        font-size: 1.2rem;
    }
    div.stButton>button {
        border-radius: 25px;
        width: 100%;
        height: 60px;
        font-size: 1.2rem;
        background-color: #4B9FE1;
        color: white;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        display: flex;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    }
    .user-message {
        background-color: #E6F7FF;
        margin-left: 20%;
        border-bottom-right-radius: 5px;
    }
    .bot-message {
        background-color: #F0F2F6;
        margin-right: 20%;
        border-bottom-left-radius: 5px;
    }
    .thinking-dots {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }
    .dot {
        height: 10px;
        width: 10px;
        background-color: #4B9FE1;
        border-radius: 50%;
        margin: 0 5px;
        animation: pulse 1.5s infinite ease-in-out;
    }
    .dot:nth-child(2) {
        animation-delay: 0.2s;
    }
    .dot:nth-child(3) {
        animation-delay: 0.4s;
    }
    @keyframes pulse {
        0% { transform: scale(0.8); opacity: 0.5; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(0.8); opacity: 0.5; }
    }
    .sidebar .sidebar-content {
        background-color: #F9F9F9;
    }
</style>
""", unsafe_allow_html=True)

# Simple AI response generator
def generate_response(user_input):
    # Simple preprocessing
    tokens = word_tokenize(user_input.lower())
    filtered_tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    processed_input = ' '.join(filtered_tokens)
    
    # Basic response patterns
    greetings = ['hi', 'hello', 'hey', 'greetings', 'howdy']
    farewells = ['bye', 'goodbye', 'see you', 'farewell']
    questions = ['what', 'how', 'why', 'when', 'where', 'who', 'which']
    
    # Check patterns and generate response
    if any(word in processed_input for word in greetings):
        return random.choice([
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Greetings! How may I assist you?",
            "Hey! I'm IRIS, your AI assistant. What's on your mind?"
        ])
    elif any(word in processed_input for word in farewells):
        return random.choice([
            "Goodbye! Have a great day!",
            "See you later! Feel free to return if you need assistance.",
            "Farewell! It was nice chatting with you.",
            "Take care! I'll be here if you need anything."
        ])
    elif "name" in processed_input:
        return "I'm IRIS, your Intelligent Responsive Interface System. How can I assist you today?"
    elif "thank" in processed_input:
        return random.choice([
            "You're welcome! Is there anything else you'd like to know?",
            "Happy to help! What else can I do for you?",
            "My pleasure! Feel free to ask if you need anything else."
        ])
    elif any(word in processed_input for word in questions):
        return random.choice([
            "That's an interesting question. Based on my understanding, I'd say it depends on several factors.",
            "Great question! From my analysis, there are multiple perspectives to consider.",
            "I've analyzed your question. While I don't have all the context, I can offer some insights.",
            "Let me think about that... Based on available information, I can provide some thoughts."
        ])
    elif "help" in processed_input or "assist" in processed_input:
        return "I'm here to help! I can answer questions, provide information, or just chat. What would you like to discuss?"
    else:
        return random.choice([
            "I understand what you're saying. Could you tell me more?",
            "That's interesting. Can you elaborate on that?",
            "I see. Is there a specific aspect of this you'd like to explore?",
            "I'm processing what you've shared. What additional information can I provide?",
            "Thank you for sharing that. Would you like me to analyze anything specific about it?"
        ])

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'is_thinking' not in st.session_state:
    st.session_state.is_thinking = False

# Load animation
lottie_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")

# Sidebar with app info
with st.sidebar:
    st.markdown("## About IRIS")
    st_lottie(lottie_animation, height=200, key="sidebar_animation")
    st.markdown("""
    IRIS (Intelligent Responsive Interface System) is a demonstration of a responsive AI with an immersive UI.
    
    **Features:**
    - Natural language processing
    - Real-time responses
    - Animated visual feedback
    - Responsive chat interface
    
    This is a simplified demo version. A full implementation would connect to more sophisticated AI models and databases.
    """)
    
    st.markdown("---")
    st.markdown("### Settings")
    response_speed = st.slider("Response Speed", min_value=1, max_value=5, value=3)
    st.markdown("### Voice Settings")
    voice_enabled = st.checkbox("Enable Voice Responses", value=False)
    if voice_enabled:
        voice_type = st.selectbox("Voice Type", ["Natural", "Robotic", "Friendly"])

# Main app area
st.markdown('<h1 class="main-title">IRIS</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Intelligent Responsive Interface System</p>', unsafe_allow_html=True)

# Display chat history
for message in st.session_state.chat_history:
    if message['is_user']:
        st.markdown(f'<div class="chat-message user-message">You: {message["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message bot-message">IRIS: {message["text"]}</div>', unsafe_allow_html=True)

# Display thinking animation if needed
if st.session_state.is_thinking:
    thinking_html = """
    <div class="chat-message bot-message" style="justify-content: flex-start; padding: 20px;">
        <div>IRIS:</div>
        <div class="thinking-dots">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        </div>
    </div>
    """
    st.markdown(thinking_html, unsafe_allow_html=True)

# User input
with st.container():
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input("Ask IRIS anything...", key="user_input")
    with col2:
        send_button = st.button("Send")

# Handle user input
if send_button and user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"text": user_input, "is_user": True})
    
    # Show thinking animation
    st.session_state.is_thinking = True
    st.experimental_rerun()

# This part is separated to show the thinking animation before displaying the response
if st.session_state.is_thinking:
    # Generate response based on user input
    thinking_time = 6 - response_speed  # Faster slider value means less thinking time
    time.sleep(thinking_time/2)  # Simulate thinking
    response = generate_response(st.session_state.chat_history[-1]["text"])
    
    # Add AI response to chat history
    st.session_state.chat_history.append({"text": response, "is_user": False})
    st.session_state.is_thinking = False
    st.experimental_rerun()
import streamlit as st
from groq import Groq
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for unique theme
st.markdown("""
    <style>
    /* Main theme colors */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Chat container */
    .chat-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* User message */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 18px;
        border-radius: 18px 18px 5px 18px;
        margin: 8px 0;
        max-width: 80%;
        float: right;
        clear: both;
    }
    
    /* Assistant message */
    .assistant-message {
        background: #f1f3f4;
        color: #202124;
        padding: 12px 18px;
        border-radius: 18px 18px 18px 5px;
        margin: 8px 0;
        max-width: 80%;
        float: left;
        clear: both;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.1);
    }
    
    /* Title styling */
    h1 {
        color: white;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = os.getenv("GROQ_API_KEY", "")

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    
    # API Key input
    api_key_input = st.text_input(
        "Groq API Key",
        value=st.session_state.groq_api_key,
        type="password",
        help="Enter your Groq API key. Get one free at https://console.groq.com"
    )
    
    if api_key_input:
        st.session_state.groq_api_key = api_key_input
    
    # Model selection
    model = st.selectbox(
        "Select Model",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"],
        help="Choose the AI model for responses"
    )
    
    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Higher values make output more random"
    )
    
    # Max tokens
    max_tokens = st.slider(
        "Max Tokens",
        min_value=100,
        max_value=4000,
        value=1024,
        step=100,
        help="Maximum length of the response"
    )
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    st.markdown("""
    ### About
    This chatbot uses Groq's ultra-fast LLM inference.
    
    **Features:**
    - 🚀 Lightning-fast responses
    - 💬 Context-aware conversations
    - 🎨 Beautiful UI
    - 🔒 Secure API key handling
    """)

# Main content
st.title("🤖 AI Chatbot")
st.markdown("##### Powered by Groq")

# Check if API key is set
if not st.session_state.groq_api_key:
    st.warning("⚠️ Please enter your Groq API key in the sidebar to start chatting.")
    st.info("""
    **How to get a Groq API key:**
    1. Visit [https://console.groq.com](https://console.groq.com)
    2. Sign up for a free account
    3. Navigate to API Keys section
    4. Create a new API key
    5. Copy and paste it in the sidebar
    """)
    st.stop()

# Initialize Groq client
try:
    client = Groq(api_key=st.session_state.groq_api_key)
except Exception as e:
    st.error(f"Error initializing Groq client: {str(e)}")
    st.stop()

# Display chat messages
for message in st.session_state.messages:
    role_class = "user-message" if message["role"] == "user" else "assistant-message"
    with st.container():
        st.markdown(
            f'<div class="{role_class}">{message["content"]}</div>',
            unsafe_allow_html=True
        )

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.container():
        st.markdown(
            f'<div class="user-message">{prompt}</div>',
            unsafe_allow_html=True
        )
    
    # Generate assistant response
    with st.spinner("Thinking..."):
        try:
            # Call Groq API
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            
            # Extract response
            assistant_response = chat_completion.choices[0].message.content
            
            # Add assistant response to chat history
            st.session_state.messages.append(
                {"role": "assistant", "content": assistant_response}
            )
            
            # Display assistant response
            with st.container():
                st.markdown(
                    f'<div class="assistant-message">{assistant_response}</div>',
                    unsafe_allow_html=True
                )
            
            # Rerun to update the display
            st.rerun()
            
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            # Remove the user message if there was an error
            st.session_state.messages.pop()

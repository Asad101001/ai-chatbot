import streamlit as st
from groq import Groq
import os
from datetime import datetime
import json
import time

# Page configuration
st.set_page_config(
    page_title="◉ NEURAL INTERFACE",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hacker/Neon Terminal Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&family=Share+Tech+Mono&display=swap');
    
    /* Main dark background */
    .stApp {
        background: #0a0e27;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(0, 255, 135, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(0, 255, 255, 0.03) 0%, transparent 50%);
        color: #00ff87;
        font-family: 'Fira Code', monospace;
    }
    
    /* Glowing text effect */
    h1, h2, h3 {
        color: #00ff87;
        text-shadow: 0 0 10px #00ff87, 0 0 20px #00ff87, 0 0 30px #00ff87;
        font-family: 'Share Tech Mono', monospace;
        letter-spacing: 3px;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0e27 0%, #1a1f3a 100%);
        border-right: 2px solid #00ff87;
        box-shadow: 0 0 20px rgba(0, 255, 135, 0.3);
    }
    
    [data-testid="stSidebar"] * {
        color: #00ffff !important;
    }
    
    /* User message - cyan neon */
    .user-message {
        background: rgba(0, 255, 255, 0.1);
        border: 1px solid #00ffff;
        border-left: 4px solid #00ffff;
        color: #00ffff;
        padding: 15px 20px;
        margin: 15px 0;
        border-radius: 5px;
        font-family: 'Fira Code', monospace;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
        animation: slideInRight 0.3s ease-out;
    }
    
    /* Assistant message - green neon */
    .assistant-message {
        background: rgba(0, 255, 135, 0.05);
        border: 1px solid #00ff87;
        border-left: 4px solid #00ff87;
        color: #00ff87;
        padding: 15px 20px;
        margin: 15px 0;
        border-radius: 5px;
        font-family: 'Fira Code', monospace;
        box-shadow: 0 0 15px rgba(0, 255, 135, 0.3);
        animation: slideInLeft 0.3s ease-out;
    }
    
    /* System message - purple neon */
    .system-message {
        background: rgba(138, 43, 226, 0.1);
        border: 1px solid #8a2be2;
        border-left: 4px solid #8a2be2;
        color: #da70d6;
        padding: 10px 15px;
        margin: 10px 0;
        border-radius: 5px;
        font-family: 'Fira Code', monospace;
        font-size: 0.85em;
        box-shadow: 0 0 10px rgba(138, 43, 226, 0.3);
    }
    
    /* Animations */
    @keyframes slideInRight {
        from { transform: translateX(50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 5px #00ff87, 0 0 10px #00ff87; }
        50% { box-shadow: 0 0 20px #00ff87, 0 0 30px #00ff87; }
    }
    
    /* Input styling */
    .stTextInput input, .stTextArea textarea {
        background: rgba(0, 20, 40, 0.8) !important;
        border: 1px solid #00ff87 !important;
        color: #00ff87 !important;
        font-family: 'Fira Code', monospace !important;
        box-shadow: 0 0 10px rgba(0, 255, 135, 0.2);
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #00ffff !important;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.4) !important;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #00ff87 0%, #00ffff 100%) !important;
        color: #0a0e27 !important;
        border: none !important;
        font-weight: bold !important;
        font-family: 'Share Tech Mono', monospace !important;
        letter-spacing: 2px;
        box-shadow: 0 0 20px rgba(0, 255, 135, 0.5);
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        animation: glow 1s ease-in-out infinite;
        transform: scale(1.05);
    }
    
    /* Select box styling */
    .stSelectbox, .stSlider {
        color: #00ffff !important;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        color: #00ff87 !important;
        text-shadow: 0 0 10px #00ff87;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #00ff87 !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        background: #0a0e27;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00ff87 0%, #00ffff 100%);
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 255, 135, 0.5);
    }
    
    /* Chat input container */
    .stChatInput {
        border: 1px solid #00ff87;
        border-radius: 5px;
        box-shadow: 0 0 15px rgba(0, 255, 135, 0.3);
    }
    
    /* Code blocks */
    code {
        color: #ff00ff !important;
        background: rgba(255, 0, 255, 0.1) !important;
    }
    
    /* Links */
    a {
        color: #00ffff !important;
        text-decoration: none !important;
        text-shadow: 0 0 5px #00ffff;
    }
    
    a:hover {
        color: #ff00ff !important;
        text-shadow: 0 0 10px #ff00ff;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = os.getenv("GROQ_API_KEY", "")

if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

if "message_count" not in st.session_state:
    st.session_state.message_count = 0

if "conversation_started" not in st.session_state:
    st.session_state.conversation_started = datetime.now()

# Sidebar
with st.sidebar:
    st.markdown("### ⚡ NEURAL INTERFACE")
    st.markdown("---")
    
    # System stats
    col1, col2 = st.columns(2)
    with col1:
        st.metric("MESSAGES", st.session_state.message_count)
    with col2:
        st.metric("TOKENS", f"{st.session_state.total_tokens:,}")
    
    st.markdown("---")
    
    # API Key input (only show if not set in .env)
    if not os.getenv("GROQ_API_KEY"):
        api_key_input = st.text_input(
            "🔑 GROQ API KEY",
            value=st.session_state.groq_api_key,
            type="password",
            help="Get free API key: https://console.groq.com"
        )
        
        if api_key_input:
            st.session_state.groq_api_key = api_key_input
        
        st.info("💡 Add GROQ_API_KEY to .env to auto-load")
    else:
        st.success("🔐 API Key loaded from .env")
    
    st.markdown("---")
    
    # Advanced model selection with descriptions
    st.markdown("### 🤖 MODEL SELECTION")
    
    model_info = {
        "llama-3.3-70b-versatile": "⚡ Latest Llama 3.3 - Most capable",
        "llama-3.3-70b-specdec": "🚀 Speculative Decoding - Ultra fast",
        "llama-3.1-70b-versatile": "💎 Llama 3.1 70B - Balanced",
        "llama-3.1-8b-instant": "⚡ Llama 3.1 8B - Lightning fast",
        "llama-3.2-90b-vision-preview": "👁️ Vision Model - Image support",
        "mixtral-8x7b-32768": "🎯 Mixtral - Long context",
        "gemma2-9b-it": "🔮 Gemma 2 - Creative",
    }
    
    model = st.selectbox(
        "Select AI Model",
        list(model_info.keys()),
        format_func=lambda x: model_info[x],
        help="Choose from latest cutting-edge models"
    )
    
    st.markdown("---")
    
    # Advanced parameters
    st.markdown("### ⚙️ PARAMETERS")
    
    temperature = st.slider(
        "🌡️ Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Creativity level (0=focused, 2=creative)"
    )
    
    max_tokens = st.slider(
        "📏 Max Tokens",
        min_value=256,
        max_value=8000,
        value=2048,
        step=256,
        help="Maximum response length"
    )
    
    top_p = st.slider(
        "🎲 Top P (Nucleus Sampling)",
        min_value=0.0,
        max_value=1.0,
        value=0.9,
        step=0.1,
        help="Diversity of responses"
    )
    
    st.markdown("---")
    
    # System prompt
    st.markdown("### 💬 SYSTEM PROMPT")
    system_prompt = st.text_area(
        "Customize AI behavior",
        value="You are a helpful AI assistant with expertise in coding, science, and technology.",
        height=100,
        help="Define how the AI should behave"
    )
    
    st.markdown("---")
    
    # Advanced features
    st.markdown("### 🎛️ FEATURES")
    
    show_thinking = st.checkbox("Show reasoning process", value=False)
    show_timestamps = st.checkbox("Show timestamps", value=True)
    stream_response = st.checkbox("Stream responses", value=True)
    
    st.markdown("---")
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ CLEAR", use_container_width=True):
            st.session_state.messages = []
            st.session_state.message_count = 0
            st.session_state.total_tokens = 0
            st.session_state.conversation_started = datetime.now()
            st.rerun()
    
    with col2:
        if st.button("💾 EXPORT", use_container_width=True):
            export_data = {
                "timestamp": datetime.now().isoformat(),
                "model": model,
                "messages": st.session_state.messages,
                "stats": {
                    "total_messages": st.session_state.message_count,
                    "total_tokens": st.session_state.total_tokens
                }
            }
            st.download_button(
                "⬇️ Download",
                data=json.dumps(export_data, indent=2),
                file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
    
    st.markdown("---")
    
    st.markdown("""
    <div style='font-size: 0.8em; color: #00ffff;'>
    <b>⚡ POWERED BY GROQ</b><br>
    Ultra-fast LLM inference<br><br>
    <b>🎯 FEATURES:</b><br>
    • Latest AI models<br>
    • Vision support<br>
    • Long context<br>
    • Real-time streaming<br>
    • Export conversations<br>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown("""
    <h1 style='text-align: center; margin-bottom: 0;'>
        ◉ NEURAL INTERFACE ◉
    </h1>
    <p style='text-align: center; color: #00ffff; font-size: 0.9em; margin-top: 0; letter-spacing: 2px;'>
        GROQ QUANTUM PROCESSING // REAL-TIME INFERENCE
    </p>
""", unsafe_allow_html=True)

# Check if API key is set
if not st.session_state.groq_api_key:
    st.markdown("""
        <div class='system-message'>
        ⚠️ SYSTEM ALERT: API KEY REQUIRED<br><br>
        <b>PERMANENT SETUP:</b><br>
        1. Create <code>.env</code> file in project root<br>
        2. Add: <code>GROQ_API_KEY=your_key_here</code><br>
        3. Restart app - key auto-loads!<br><br>
        <b>OR</b> enter key in sidebar (temporary)<br><br>
        Get free key: <a href='https://console.groq.com' target='_blank'>console.groq.com</a>
        </div>
    """, unsafe_allow_html=True)
    st.stop()

# Initialize Groq client
try:
    client = Groq(api_key=st.session_state.groq_api_key)
except Exception as e:
    st.error(f"Error initializing Groq client: {str(e)}")
    st.stop()

# Display chat messages
for idx, message in enumerate(st.session_state.messages):
    role_class = "user-message" if message["role"] == "user" else "assistant-message"
    
    timestamp_html = ""
    if show_timestamps and "timestamp" in message:
        timestamp_html = f"<div style='font-size: 0.75em; opacity: 0.7; margin-bottom: 5px;'>[{message['timestamp']}]</div>"
    
    role_indicator = ">> USER:" if message["role"] == "user" else ">> ASSISTANT:"
    
    with st.container():
        st.markdown(
            f'<div class="{role_class}">{timestamp_html}<b>{role_indicator}</b><br>{message["content"]}</div>',
            unsafe_allow_html=True
        )

# Chat input
if prompt := st.chat_input(">>> ENTER COMMAND..."):
    # Add timestamp
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Add user message to chat history
    st.session_state.messages.append({
        "role": "user", 
        "content": prompt,
        "timestamp": current_time
    })
    st.session_state.message_count += 1
    
    # Display user message
    with st.container():
        timestamp_html = f"<div style='font-size: 0.75em; opacity: 0.7; margin-bottom: 5px;'>[{current_time}]</div>" if show_timestamps else ""
        st.markdown(
            f'<div class="user-message">{timestamp_html}<b>>> USER:</b><br>{prompt}</div>',
            unsafe_allow_html=True
        )
    
    # Generate assistant response
    with st.spinner("◉ PROCESSING NEURAL PATTERNS..."):
        try:
            # Prepare messages with system prompt
            messages_to_send = [{"role": "system", "content": system_prompt}]
            messages_to_send.extend([
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ])
            
            start_time = time.time()
            
            # Call Groq API with advanced parameters
            chat_completion = client.chat.completions.create(
                messages=messages_to_send,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                stream=stream_response,
            )
            
            # Handle streaming vs non-streaming response
            if stream_response:
                response_placeholder = st.empty()
                full_response = ""
                
                for chunk in chat_completion:
                    if chunk.choices[0].delta.content:
                        full_response += chunk.choices[0].delta.content
                        response_placeholder.markdown(
                            f'<div class="assistant-message"><b>>> ASSISTANT:</b><br>{full_response}▊</div>',
                            unsafe_allow_html=True
                        )
                
                assistant_response = full_response
                response_placeholder.markdown(
                    f'<div class="assistant-message"><b>>> ASSISTANT:</b><br>{assistant_response}</div>',
                    unsafe_allow_html=True
                )
                
                # Estimate tokens for streaming (rough approximation)
                tokens_used = len(assistant_response.split()) * 1.3
            else:
                assistant_response = chat_completion.choices[0].message.content
                tokens_used = chat_completion.usage.total_tokens if hasattr(chat_completion, 'usage') else 0
                
                response_time = time.time() - start_time
                
                # Display response with metrics
                timestamp_html = f"<div style='font-size: 0.75em; opacity: 0.7; margin-bottom: 5px;'>[{datetime.now().strftime('%H:%M:%S')}] • Response time: {response_time:.2f}s</div>" if show_timestamps else ""
                
                with st.container():
                    st.markdown(
                        f'<div class="assistant-message">{timestamp_html}<b>>> ASSISTANT:</b><br>{assistant_response}</div>',
                        unsafe_allow_html=True
                    )
            
            # Add assistant response to chat history
            st.session_state.messages.append({
                "role": "assistant", 
                "content": assistant_response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            st.session_state.message_count += 1
            st.session_state.total_tokens += int(tokens_used)
            
            # Show thinking process if enabled
            if show_thinking and not stream_response:
                with st.expander("🧠 View Reasoning Process"):
                    st.json({
                        "model": model,
                        "temperature": temperature,
                        "tokens_used": int(tokens_used),
                        "response_time": f"{response_time:.2f}s",
                        "prompt_length": len(prompt),
                        "response_length": len(assistant_response)
                    })
            
            # Rerun to update the display
            st.rerun()
            
        except Exception as e:
            error_msg = str(e)
            st.markdown(
                f'<div class="system-message">❌ ERROR: {error_msg}</div>',
                unsafe_allow_html=True
            )
            # Remove the user message if there was an error
            st.session_state.messages.pop()
            st.session_state.message_count -= 1

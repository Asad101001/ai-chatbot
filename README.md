# ⚡ NEURAL INTERFACE - AI Chatbot

A cutting-edge AI chatbot with **hacker-themed neon terminal UI**, powered by Groq's ultra-fast inference and the latest LLM models.

![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.40.0-red.svg)
![Groq](https://img.shields.io/badge/groq-latest-blue.svg)

## ✨ Features

### 🎨 Unique Hacker Theme
- **Neon terminal aesthetic** with cyan/green glow effects
- **Matrix-style interface** inspired by cyberpunk films
- **Animated messages** with smooth transitions
- **Custom cyberpunk font** (Fira Code, Share Tech Mono)

### 🤖 Latest AI Models (2025)
- `llama-3.3-70b-versatile` - Most capable Llama model
- `llama-3.3-70b-specdec` - Ultra-fast speculative decoding
- `llama-3.2-90b-vision-preview` - Vision support for images
- `mixtral-8x7b-32768` - Long context window (32K tokens)
- `gemma2-9b-it` - Google's creative model
- Plus more!

### 🚀 Advanced Functionality
- ✅ **Permanent API key storage** (auto-loads from .env)
- ✅ **Real-time streaming responses**
- ✅ **Custom system prompts**
- ✅ **Message timestamps**
- ✅ **Token counting & statistics**
- ✅ **Export conversations** (JSON format)
- ✅ **Reasoning process viewer**
- ✅ **Advanced parameters** (temperature, top_p, max_tokens)
- ✅ **Response time metrics**

### 🔐 Security
- Environment variable storage
- Never commit API keys
- Local-only sensitive data

---

## 🎯 Screenshots

**Hacker Terminal Interface:**
```
◉ NEURAL INTERFACE ◉
GROQ QUANTUM PROCESSING // REAL-TIME INFERENCE

>> USER:
[13:37:42] What is quantum computing?

>> ASSISTANT:
[13:37:43] • Response time: 0.87s
Quantum computing uses quantum-mechanical phenomena...
```

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/Asad101001/ai-chatbot.git
cd ai-chatbot
```

### 2. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up API Key (Permanent)
```bash
# Copy template
cp .env.example .env

# Edit .env and add your key
echo "GROQ_API_KEY=your_key_here" > .env
```

Get free key: **https://console.groq.com**

### 4. Run!
```bash
streamlit run app.py
```

---

## 🎛️ Features Breakdown

### Sidebar Controls

**Model Selection:**
- 7 latest models including vision support
- Each with performance indicators

**Advanced Parameters:**
- 🌡️ Temperature (0-2.0)
- 📏 Max Tokens (256-8000)
- 🎲 Top P / Nucleus Sampling (0-1.0)

**System Prompt:**
- Customize AI personality
- Define expertise areas
- Set response style

**Features Toggle:**
- Show reasoning process
- Display timestamps
- Stream responses

**Actions:**
- 🗑️ Clear chat history
- 💾 Export conversations (JSON)

### Live Statistics
- Total messages sent
- Total tokens used
- Conversation duration

---

## 📁 Project Structure

```
ai-chatbot/
├── app.py                  # Main application (hacker theme)
├── requirements.txt        # Latest dependencies
├── .env                    # Your API key (create this)
├── .gitignore              # Security (prevents .env commit)
└── README.md               # This file
```

---

## 🎨 Customization

### Change Colors

Edit CSS in `app.py`:
```python
# Current: Cyan/Green neon
color: #00ff87;  # Change to your color
text-shadow: 0 0 10px #00ff87;  # Glow effect
```

**Color Schemes:**
- **Cyan/Green** (current): `#00ff87`, `#00ffff`
- **Red/Orange**: `#ff0000`, `#ff6600`
- **Purple/Pink**: `#8a2be2`, `#ff1493`
- **Blue/White**: `#00bfff`, `#ffffff`

### Add Your Own Models

```python
model_info = {
    "your-model-name": "🎯 Your Model - Description",
    # Add more...
}
```

### Custom System Prompts

Edit default in sidebar section:
```python
system_prompt = st.text_area(
    "Customize AI behavior",
    value="Your custom prompt here",
    ...
)
```

---

## 🚢 Deployment

### Streamlit Cloud (Free)

1. Push to GitHub
2. Visit **https://share.streamlit.io**
3. Connect repository
4. Add secrets:
   ```toml
   GROQ_API_KEY = "your_key_here"
   ```
5. Deploy!

### Other Platforms
- **Railway**: Auto-deploy from GitHub
- **Render**: Use Streamlit template
- **Heroku**: Add Procfile

---

## 🔧 Advanced Usage

### Export Conversations

Click **💾 EXPORT** in sidebar:
```json
{
  "timestamp": "2025-02-14T13:37:42",
  "model": "llama-3.3-70b-versatile",
  "messages": [...],
  "stats": {
    "total_messages": 42,
    "total_tokens": 15234
  }
}
```

### View Reasoning Process

Enable "Show reasoning process":
```json
{
  "model": "llama-3.3-70b-versatile",
  "temperature": 0.7,
  "tokens_used": 523,
  "response_time": "0.87s",
  "prompt_length": 45,
  "response_length": 312
}
```

### Streaming Responses

Enable "Stream responses" for real-time output:
- See text appear word-by-word
- Lower perceived latency
- Better UX for long responses

---

## 🆚 Groq vs OpenAI

| Feature | Groq | OpenAI |
|---------|------|--------|
| **Speed** | ⚡ Ultra-fast (2-3x faster) | 🐢 Standard |
| **Cost** | ✅ Free tier | 💰 Pay per token |
| **Models** | Llama 3.3, Mixtral, Gemma | GPT-4, GPT-3.5 |
| **Context** | Up to 32K tokens | Up to 128K tokens |
| **Best For** | Speed, demos, learning | Production, quality |

**Recommendation:** Start with Groq (free + fast), upgrade to OpenAI if needed.

---

## 🐛 Troubleshooting

### API Key Not Loading

```bash
# Check .env exists
ls -la | grep .env

# Verify content
cat .env

# Should show:
GROQ_API_KEY=gsk_...
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Port In Use

```bash
# Use different port
streamlit run app.py --server.port 8502
```

### Streaming Not Working

- Disable "Stream responses" in sidebar
- Check internet connection
- Try different model

---

## 🎓 Learning Resources

**Beginner:**
- Change colors in CSS
- Try different models
- Export a conversation

**Intermediate:**
- Add new models
- Customize system prompts
- Modify UI layout

**Advanced:**
- Add image upload support
- Implement RAG (document Q&A)
- Create multi-agent chat

---

## 🙏 Credits

- **Groq** - Ultra-fast LLM inference
- **Meta AI** - Llama models
- **Streamlit** - Web framework
- **Google** - Gemma models
- **Mistral AI** - Mixtral models

---

## ⚡ Why "Neural Interface"?

Inspired by cyberpunk aesthetics and hacker culture, this interface transforms boring chatbots into an immersive terminal experience. The neon glow, monospace fonts, and dark theme create a futuristic atmosphere perfect for AI interaction.

---

**Built with 💚 by developers who love terminals**

**Questions?** Open an issue on GitHub  
**Love it?** Star the repo ⭐  
**Want more?** Check out the features and customize away!

---

```
◉ SYSTEM READY // NEURAL LINK ESTABLISHED ◉
```
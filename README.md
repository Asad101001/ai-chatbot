# 🤖 AI Chatbot with Streamlit & Groq

A beautiful, minimal AI chatbot built with Streamlit and powered by Groq's ultra-fast LLM inference API.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🚀 **Lightning-fast responses** using Groq's LPU inference
- 💬 **Context-aware conversations** with chat history
- 🎨 **Beautiful gradient UI** with custom theme
- 🔒 **Secure API key handling** via environment variables
- ⚙️ **Customizable parameters** (model, temperature, max tokens)
- 📱 **Responsive design** that works on all devices

## 🎯 Demo

The chatbot supports multiple Groq models:
- `llama-3.3-70b-versatile` - Most capable model
- `llama-3.1-8b-instant` - Fast and efficient
- `mixtral-8x7b-32768` - Great for long contexts

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API key (free at [console.groq.com](https://console.groq.com))
- Git (for version control)

## 🚀 Local Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-chatbot.git
cd ai-chatbot
```

### Step 2: Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Groq API key:
```
GROQ_API_KEY=your_actual_groq_api_key_here
```

**How to get a Groq API key:**
1. Visit [https://console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to "API Keys" section
4. Click "Create API Key"
5. Copy the key and paste it in your `.env` file

### Step 5: Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## 🔧 Configuration

You can customize the chatbot behavior in the sidebar:

- **Model Selection**: Choose between different LLM models
- **Temperature**: Control randomness (0.0 = focused, 2.0 = creative)
- **Max Tokens**: Set maximum response length
- **API Key**: Enter your Groq API key (if not using .env)

## 📁 Project Structure

```
ai-chatbot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

## 🐳 Alternative: Using OpenAI API

To use OpenAI instead of Groq, modify `app.py`:

1. Replace `from groq import Groq` with `from openai import OpenAI`
2. Replace `client = Groq(api_key=...)` with `client = OpenAI(api_key=...)`
3. Update model names to OpenAI models (e.g., "gpt-4", "gpt-3.5-turbo")

## 🚢 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your `GROQ_API_KEY` in the Secrets section
5. Deploy!

### Deploy to Other Platforms

- **Heroku**: Add `setup.sh` and `Procfile`
- **Railway**: Connect GitHub repo directly
- **Render**: Use their Streamlit template

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Groq](https://groq.com/) for ultra-fast LLM inference
- [Meta AI](https://ai.meta.com/) for the Llama models

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/YOUR_USERNAME/ai-chatbot](https://github.com/YOUR_USERNAME/ai-chatbot)

---

**Note**: Keep your API keys secure and never commit them to version control!

# 🚀 Quick Start Cheat Sheet

## First Time Setup (5 minutes)

```bash
# 1. Clone or download the project
git clone https://github.com/YOUR_USERNAME/ai-chatbot.git
cd ai-chatbot

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up API key
cp .env.example .env
# Edit .env and add your Groq API key

# 6. Run the app
streamlit run app.py
```

## Get Groq API Key

1. Visit: https://console.groq.com
2. Sign up (free)
3. Go to "API Keys" → "Create API Key"
4. Copy the key

## Daily Usage

```bash
# Activate environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run app
streamlit run app.py

# Stop app
Ctrl + C
```

## Git Commands

```bash
# Initial setup
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ai-chatbot.git
git push -u origin main

# Daily workflow
git add .
git commit -m "Your changes description"
git push
```

## Common Issues

**Issue:** `streamlit: command not found`
**Fix:** Make sure venv is activated

**Issue:** API key error
**Fix:** Check `.env` file has correct key without extra spaces

**Issue:** Port in use
**Fix:** `streamlit run app.py --server.port 8502`

## File Structure

```
ai-chatbot/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .env               # Your API key (don't commit!)
├── .env.example       # Template
├── .gitignore         # Git ignore rules
├── README.md          # Documentation
└── SETUP_GUIDE.md     # Detailed guide
```

## Customization

**Change colors:** Edit CSS in `app.py` (line 15-70)
**Add models:** Edit model list in `app.py` (line 104)
**Change defaults:** Edit sidebar parameters (line 110-130)

## Deployment

**Streamlit Cloud (Free):**
1. Push code to GitHub
2. Visit: https://share.streamlit.io
3. Connect repository
4. Add secrets (GROQ_API_KEY)
5. Deploy!

**Alternative:** Use Groq's OpenAI-compatible API

Replace Groq with OpenAI in app.py:
- Model: `gpt-4` or `gpt-3.5-turbo`
- API Key: OpenAI API key

---

**Documentation:** See SETUP_GUIDE.md for detailed instructions
**Help:** Check troubleshooting section in SETUP_GUIDE.md

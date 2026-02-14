# 📚 Complete Setup Guide

This guide walks you through every step of setting up and deploying your AI chatbot.

## 📑 Table of Contents

1. [Local Testing](#local-testing)
2. [GitHub Setup](#github-setup)
3. [Best Practices](#best-practices)
4. [Troubleshooting](#troubleshooting)

---

## 🖥️ Local Testing

### Step 1: Verify Python Installation

```bash
# Check Python version (should be 3.8+)
python --version
# or
python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

### Step 2: Create Project Directory

```bash
# Create and navigate to project folder
mkdir ai-chatbot
cd ai-chatbot
```

### Step 3: Set Up Virtual Environment

**Why use a virtual environment?**
- Isolates project dependencies
- Prevents conflicts with other projects
- Makes deployment easier

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 4: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### Step 5: Get Your Groq API Key

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up with your email or Google account (it's free!)
3. Navigate to "API Keys" in the left sidebar
4. Click "Create API Key"
5. Give it a name (e.g., "Chatbot App")
6. Copy the key immediately (you won't see it again!)

### Step 6: Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your favorite editor
# Windows: notepad .env
# macOS: open -e .env
# Linux: nano .env
```

Replace `your_groq_api_key_here` with your actual API key:
```
GROQ_API_KEY=gsk_youractualapikeyhere123456789
```

### Step 7: Run the Application

```bash
streamlit run app.py
```

Expected output:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

### Step 8: Test the Chatbot

1. Your browser should open automatically to `http://localhost:8501`
2. If the API key is set in `.env`, it should work immediately
3. Otherwise, enter your API key in the sidebar
4. Try sending a message: "Hello, how are you?"
5. Test different settings (models, temperature, etc.)

### Step 9: Stop the Application

Press `Ctrl + C` in the terminal to stop the server.

---

## 🐙 GitHub Setup

### Step 1: Install Git

Check if Git is installed:
```bash
git --version
```

If not, download from [git-scm.com](https://git-scm.com/downloads)

### Step 2: Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click the "+" icon → "New repository"
3. Name it: `ai-chatbot`
4. Description: "Minimal AI chatbot with Streamlit and Groq"
5. Choose "Public" or "Private"
6. **DO NOT** initialize with README, .gitignore, or license
7. Click "Create repository"

### Step 4: Initialize Local Git Repository

```bash
# Navigate to your project directory
cd ai-chatbot

# Initialize git
git init

# Add all files
git add .

# Check what will be committed
git status

# Make your first commit
git commit -m "Initial commit: AI chatbot with Streamlit and Groq"
```

### Step 5: Connect to GitHub

Replace `YOUR_USERNAME` with your GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/ai-chatbot.git

# Verify the remote
git remote -v
```

### Step 6: Push to GitHub

```bash
# Push to main branch
git branch -M main
git push -u origin main
```

You may be prompted for GitHub credentials:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your GitHub password)

### Step 7: Create Personal Access Token (if needed)

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Name: "AI Chatbot Repo"
4. Select scopes: `repo` (all sub-options)
5. Click "Generate token"
6. Copy the token and use it as your password

### Step 8: Verify on GitHub

1. Go to `https://github.com/YOUR_USERNAME/ai-chatbot`
2. You should see all your files
3. Check that `.env` is NOT visible (it's in .gitignore)

---

## 💡 Best Practices

### Security

✅ **DO:**
- Keep API keys in `.env` file
- Add `.env` to `.gitignore`
- Use environment variables for secrets
- Share `.env.example` instead of `.env`

❌ **DON'T:**
- Commit API keys to Git
- Share your `.env` file
- Hardcode secrets in code
- Push sensitive data to GitHub

### Git Workflow

```bash
# Before making changes
git status
git pull

# After making changes
git add .
git commit -m "Descriptive message about what changed"
git push

# Check your git history
git log --oneline
```

### Good Commit Messages

✅ Good:
```
feat: Add temperature control slider
fix: Resolve API key validation issue
docs: Update README with deployment instructions
style: Improve chat message styling
```

❌ Bad:
```
update
fixed stuff
changes
asdf
```

### Code Organization

- Keep `app.py` focused on UI logic
- Separate API calls into functions
- Use meaningful variable names
- Add comments for complex logic
- Follow PEP 8 style guide

### Testing Checklist

Before committing:
- [ ] App runs without errors
- [ ] API key handling works correctly
- [ ] All features function as expected
- [ ] No sensitive data in code
- [ ] README is up to date
- [ ] Dependencies are in requirements.txt

---

## 🔧 Troubleshooting

### Issue: "streamlit: command not found"

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "ModuleNotFoundError: No module named 'groq'"

**Solution:**
```bash
pip install groq
```

### Issue: API Key Not Working

**Checklist:**
- [ ] API key is copied correctly (no extra spaces)
- [ ] `.env` file is in the project root directory
- [ ] Environment variable is loaded correctly
- [ ] API key is valid (check Groq console)

### Issue: Git Push Fails

**Solutions:**

1. **Authentication error:**
```bash
# Use Personal Access Token instead of password
git remote set-url origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/ai-chatbot.git
```

2. **Rejected push:**
```bash
git pull origin main --rebase
git push origin main
```

### Issue: Port Already in Use

**Solution:**
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

### Issue: Chat Messages Not Displaying

**Solution:**
- Clear browser cache
- Try incognito/private mode
- Check browser console for errors (F12)

---

## 🎓 Next Steps

1. **Customize the theme** - Edit CSS in `app.py`
2. **Add features** - File uploads, voice input, etc.
3. **Deploy online** - Use Streamlit Cloud (free)
4. **Share with friends** - Send them the GitHub link

---

## 📞 Getting Help

- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Groq Docs**: [console.groq.com/docs](https://console.groq.com/docs)
- **Git Docs**: [git-scm.com/doc](https://git-scm.com/doc)

---

**Happy Coding! 🚀**

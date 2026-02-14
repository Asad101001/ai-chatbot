# Alternative Configuration: Using OpenAI Instead of Groq

If you prefer to use OpenAI's API instead of Groq, follow these instructions.

## Changes Required

### 1. Update requirements.txt

Replace:
```
groq==0.4.2
```

With:
```
openai==1.12.0
```

### 2. Update .env file

Replace:
```
GROQ_API_KEY=your_groq_api_key_here
```

With:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Modify app.py

**Line 2:** Change import
```python
from openai import OpenAI
```

**Line 52:** Update session state key
```python
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = os.getenv("OPENAI_API_KEY", "")
```

**Line 58-62:** Update API key input
```python
api_key_input = st.text_input(
    "OpenAI API Key",
    value=st.session_state.openai_api_key,
    type="password",
    help="Enter your OpenAI API key. Get one at https://platform.openai.com"
)

if api_key_input:
    st.session_state.openai_api_key = api_key_input
```

**Line 67-69:** Update model selection
```python
model = st.selectbox(
    "Select Model",
    ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"],
    help="Choose the AI model for responses"
)
```

**Line 109:** Update title
```python
st.markdown("##### Powered by OpenAI")
```

**Line 112:** Update check
```python
if not st.session_state.openai_api_key:
    st.warning("⚠️ Please enter your OpenAI API key in the sidebar to start chatting.")
```

**Line 114-120:** Update info message
```python
st.info("""
**How to get an OpenAI API key:**
1. Visit [https://platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Go to API keys section
4. Create new secret key
5. Copy and paste it in the sidebar
""")
```

**Line 125-126:** Update client initialization
```python
try:
    client = OpenAI(api_key=st.session_state.openai_api_key)
```

**Line 153-159:** Update API call (use same format)
```python
chat_completion = client.chat.completions.create(
    messages=[
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ],
    model=model,
    temperature=temperature,
    max_tokens=max_tokens,
)
```

## Get OpenAI API Key

1. Go to https://platform.openai.com
2. Sign up or log in
3. Navigate to "API Keys"
4. Click "Create new secret key"
5. Copy the key immediately
6. Add it to your `.env` file

## Cost Comparison

**Groq:**
- ✅ Free tier available
- ✅ Very fast inference
- ⚠️ Limited models

**OpenAI:**
- ⚠️ Pay per use
- ✅ Most capable models (GPT-4)
- ✅ More reliable
- ✅ Better for production

## Pricing (OpenAI)

- **GPT-3.5 Turbo:** $0.0005 / 1K tokens (input), $0.0015 / 1K tokens (output)
- **GPT-4:** $0.03 / 1K tokens (input), $0.06 / 1K tokens (output)
- **GPT-4 Turbo:** $0.01 / 1K tokens (input), $0.03 / 1K tokens (output)

Example: 100 conversations (~50K tokens) with GPT-3.5 = ~$0.50

## Why Choose Groq?

- Free to use
- Extremely fast (2-3x faster than OpenAI)
- Good for demos and learning
- Great for high-throughput applications

## Why Choose OpenAI?

- More established and reliable
- Better model quality (GPT-4)
- More features (function calling, vision, etc.)
- Better for production applications

## Recommendation

**For learning/demos:** Use Groq (free and fast)
**For production:** Use OpenAI (more reliable)

You can easily switch between them by changing the code!

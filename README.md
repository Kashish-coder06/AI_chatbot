# AI_chatbot
# Personal AI Chatbot - KashishBot 🤖

KashishBot is a **personal AI assistant** built using the **Groq API**.  
It can chat with you, remember context, and perform small tasks like telling the time or jokes.  

---

## Features

- **Memory/Context**: Remembers the last 20 messages for natural conversations.  
- **Custom Persona**: Friendly, helpful, and sometimes playful AI assistant.  
- **Command Shortcuts**:  
  - `time` – Shows current system time.  
  - `joke` – Tells a funny joke.  
  - Easily extendable for new commands.  
- **Environment Variables**: Securely stores your API key using a `.env` file.  
- **Multi-turn Conversations**: AI remembers conversation history to provide context-aware replies.



## Setup

1. **Clone the repository**

bash
git clone https://github.com/yourusername/personal-ai-chatbot.git
cd personal-ai-chatbot


2. **Install dependencies**

bash
pip install groq python-dotenv

3. **Create a `.env` file**

```env
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the chatbot**

```bash
python main.py
```

---

## Usage

* Start the chatbot:

```bash
python main.py
```

* Chat with the assistant:

```
You: Hello!
AI: Hello! How can I help you today?
```




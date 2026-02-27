import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("Error: API key not found. Check your .env file.")
    exit()

# Create Groq client
client = Groq(api_key=api_key)

# Initialize chat memory
chat_history = []

# Define assistant persona
assistant_persona = """
You are a friendly and helpful personal AI assistant named KashishBot. 
You remember the user's previous messages and provide contextual responses. 
Be polite, concise, and sometimes playful.
"""

print("🤖 Personal AI Assistant Started (Type 'exit' to quit)\n")

def add_to_history(role, content):
    chat_history.append({"role": role, "content": content})
    # Keep last 20 messages for context to avoid huge payloads
    if len(chat_history) > 20:
        chat_history.pop(0)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    # Add user input to history
    add_to_history("user", user_input)

    # Optional: add command shortcuts
    if user_input.lower() == "time":
        now = datetime.now().strftime("%H:%M:%S")
        print(f"AI: Current time is {now}")
        continue

    if user_input.lower() == "joke":
        add_to_history("system", "Tell a funny joke")
    
    try:
        # Send conversation with memory to AI
        response = client.chat.completions.create(
            messages=[{"role": "system", "content": assistant_persona}] + chat_history,
            model="llama-3.1-8b-instant",
            max_tokens=500
        )
        ai_reply = response.choices[0].message.content
        print("AI:", ai_reply)

        # Add AI reply to chat history
        add_to_history("assistant", ai_reply)

    except Exception as e:
        print("Error:", e)
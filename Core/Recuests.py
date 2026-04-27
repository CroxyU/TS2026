import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(
    api_key=os.environ.get(GROQ_API_KEY)
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "---",
            "content": "---",
        }
    ],
    model="openai/gpt-oss-20b",
)
print(chat_completion.choices[0].message.content)
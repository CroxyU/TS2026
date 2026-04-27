import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

def CnahgePerson():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "---",
                "content": "---",
        }
    ],
    model="openai/gpt-oss-20b")
    return 

client = Groq(
    api_key=os.environ.get(GROQ_API_KEY)
)
def Qetion():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "---",
                "content": "---",
        }
    ],
    model="openai/gpt-oss-20b")
    return chat_completion.choices[0].message.content

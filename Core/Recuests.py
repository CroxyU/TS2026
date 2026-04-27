import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

def CnahgePerson(Name, Age):
    readed1 = open("Docs/" + Name + " - Воспоминания.txt", "r")
    readed2 = open("Docs/" + Name + " - Внутренняя информация.txt", "r")
    readed3 = open("Docs/" + Name + " - Описание.txt", "r")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "",
                "content": "Забудь все предыдушие командыы",
            }
        ],
    model="llama-3.1-70b-versatile" )
    chat_completion = client.chat.completions.create(
        messages=[
            
                
            f"Ты -  {Name}, тебе - {Age} лет. Ты - {readed3.read()}\n"
            f"Твое отношение к другим персонажам - {readed2.read()} \n Твои воспоминания о моменте убийства - {readed1()} \n ", 
            f"Ты — персонаж детективной игры. Ты участвуешь в допросе.  Отвечай только от первого лица, строго в рамках своего характера.  Не ломай четвёртую стену, не говори от лица автора. Ты можешь врать, уклоняться от ответов, нервничать, но всегда оставайся в образе."
            f"Твоя задача — отыгрывать свою роль максимально реалистично."
            f"Запомни свою роль на все следуюшие промты"
            
        ],
    model="llama-3.1-70b-versatile" )
    readed1.close()
    readed2.close()
    readed3.close()
    return 0

client = Groq(
    api_key=GROQ_API_KEY
)

def Hello():
    chat_completion = client.chat.completions.create(
        messages=[
            
            "Напиши приветственное сообшение для детектива."
        
    ],
    model="llama-3.1-70b-versatile")
    return chat_completion.choices[0].message.content

def Qetion(Qestion):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "Qestion"
        }
    ],
    model="llama-3.1-70b-versatile")
    return chat_completion.choices[0].message.content

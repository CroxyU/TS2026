from core.config import GROQ_API_KEY
from groq import Groq

client = Groq(
    api_key=GROQ_API_KEY
)
Ages  = {"Angela":36,"Meredict":46,"Sesil":56, "Fillip":46, "Elsa":46,}


def ChangePerson(Name):
    readed1 = open("Docs/" + Name + " - Воспоминания.txt", "r", encoding="utf-8")
    readed2 = open("Docs/" + Name + " - Внутренняя информация.txt", "r", encoding="utf-8")
    readed3 = open("Docs/" + Name + " - Описание.txt", "r", encoding="utf-8")
    
    prompt = (f"Тебе - {Ages[Name]} лет. Ты - {readed3.read()}\n"
        f"Твое отношение к другим персонажам - {readed2.read()} \n Твои воспоминания о моменте убийства - {readed1.read()} \n "
        f"Ты — персонаж детективной игры. Ты участвуешь в допросе.  Отвечай только от первого лица, строго в рамках своего характера. Не ломай четвёртую стену, не говори от лица автора. Ты можешь врать, уклоняться от ответов, нервничать, но всегда оставайся в образе."
        f"Твоя задача — отыгрывать свою роль максимально реалистично."
        f"Запомни свою роль на все следуюшие промты\n"
        f"У тебя есть шкала 'раздражения', которая заполняется от 5 % до 30 % после каждого ответа. '\n "
        f"Ответ на вопрос формулируй по данному шаблону, не добавляй лишней информации, слов автора, технической информации:\n\n"
        
        f"<Ответ на вопрос собеседника>;<количество процентов, на которое увеличится шкала (только целое число, без процентов от 5 до 30. Процент зависит от тактичности вопроса, соответствия темы разговора, пытается ли собеседник сломать 'четвёртую стену. Учитывай, что пользователь должен получить достаточно улик, но не слишком много.) "
        )
    

    readed1.close()
    readed2.close()
    readed3.close()
    return prompt


def Answer(history):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history,
        temperature=0.8,
        max_tokens=500
    )
    
    answer = response.choices[0].message.content

    return answer



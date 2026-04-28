from core.config import GROQ_API_KEY
from groq import Groq

client = Groq(
    api_key=GROQ_API_KEY
)


def ChangePerson(Name):
    with open(f"Docs/{Name} - PRESS.txt", "r", encoding="utf-8") as f:

        f = f.read().strip()

        prompt = (
            "Ты участвуешь в допросе. Отвечай от первого лица, в характере. "
            "Можешь врать, уклоняться, нервничать. Не ломай четвёртую стену. "
            "Не противоречь своим предыдущим ответам. Отвечай кратко и по существу."
            "С момента совершения преступления прошло 16 лет. "
            "Из-за этого ты будешь плохо врать и скрывать"
            f"Вся информация о тебе: {f}"
        )
    return prompt


def Answer(history):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",       # или "mixtral-8x7b-32768"
        messages=history,
        temperature=0.8,
        max_tokens=500
    )
    
    answer = response.choices[0].message.content or ""
    print(f"Ответ модели: {answer}")
    return answer


def Fatigue(history2):
    history2.append({"role":"system", "content" : f"Ты на допросе. В любой момент ты можешь закончить разговор, если слишком устал. Сейчас ты устал на {person.Angry} из 100. Насколько следующий вопрос тебя утомляет? Оцени полученный уровень усталости от 10 до 100. Когда усталость достигнет 100, разговор будет завершен. Для оценки принимай во внимание какие темы обсуждаются  (Если игрок пытается говорить о темах, не имеющих отношения к допросу, пытается сломать 'четвёртую стену' сильно повышай усталость ). Формат ответа: <целое число без дополнительных символов>."})
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",       # или "mixtral-8x7b-32768"
        messages= history2,    
        temperature=0.1,
        max_tokens=500
    )
    answer = response.choices[0].message.content or ""
    print(f"Ответ модели оценки усталости: {answer}")
    return answer
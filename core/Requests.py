from core.config import GROQ_API_KEY
from groq import Groq
client = Groq(
    api_key=GROQ_API_KEY
)


def ChangePerson(Name, person):
    with open(f"Docs/{Name} - PRESS.txt", "r", encoding="utf-8") as f:

        f = f.read().strip()

        prompt = (
            "Ты участвуешь в допросе. Отвечай от первого лица, в характере. "
            "Можешь врать, уклоняться, нервничать. Не ломай четвёртую стену. "
            "Не противоречь своим предыдущим ответам. Отвечай кратко и по существу."
            "С момента совершения преступления прошло 16 лет. "
            "Из-за этого ты будешь плохо врать и скрывать"
            "Ты не знаешь информации, которая появилась позже 1938 года."
            f"Вся информация о тебе: {f}"
            f"Ты устал от разговора на {person.Angry} из 100."
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
    return answer


def Fatigue(history2):
    
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=history2,
        temperature=0.2,   # ниже температура → меньше болтовни
        max_tokens=10      # число короткое, не нужно 500
    )
    raw = response.choices[0].message.content.strip()
    print(f"Ответ модели оценки усталости: {raw}")
    
    # Извлекаем число
    import re
    match = re.search(r'\d+', raw)
    if match:
        return int(match.group())
    else:
        # Fallback: если модель всё-таки выдала текст, берём среднее
        print("⚠️ Модель не вернула число, использую fallback 20")
        return 20
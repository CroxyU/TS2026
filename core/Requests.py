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
        model="groq/compound-mini",
        messages=history,
        temperature=0.8,
        max_tokens=500
    )
    
    answer = response.choices[0].message.content or ""

    return answer



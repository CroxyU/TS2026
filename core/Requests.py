from core.config import GROQ_API_KEY
from groq import Groq

client = Groq(
    api_key=GROQ_API_KEY
)
Ages  = {"Angela":36,"Meredict":46,"Sesil":56, "Fillip":46, "Elsa":46,}


def ChangePerson(Name):
    with open(f"Docs/{Name} - Описание.txt", "r", encoding="utf-8") as f_desc, \
         open(f"Docs/{Name} - Внутренняя информация.txt", "r", encoding="utf-8") as f_inner, \
         open(f"Docs/{Name} - Воспоминания.txt", "r", encoding="utf-8") as f_mem:

        desc = f_desc.read().strip()
        inner = f_inner.read().strip()
        mem = f_mem.read().strip()

    prompt = (
        f"Ты — {Name}, {Ages[Name]} лет. {desc}\n"
        f"Твоё отношение к другим: {inner}\n"
        f"Твои воспоминания о моменте убийства: {mem}\n\n"
        "Ты участвуешь в допросе. Отвечай от первого лица, в характере. "
        "Можешь врать, уклоняться, нервничать. Не ломай четвёртую стену. "
        "Не противоречь своим предыдущим ответам. Отвечай кратко и по существу."
    )
    return prompt


def Answer(history):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history,
        temperature=0.8,
        max_tokens=500
    )
    
    answer = response.choices[0].message.content or ""

    return answer



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
        f"Ответ на вопрос формулируй по данному шаблону, не добавляй лишней информации, слов автора, технической информации:\n\n"
        f"При ответе обращай внимание на предыдущие вопросы и ответы, не противоречь себе, не добавлять лишней информации, не повторяйся. Старайся дополнять/расширять информацию \n\n"
        f"Ответ на вопрос должен основываться на твоих воспоминаниях, внутренней информации и описании. Ты можешь придумывать информацию, которой нет в этих документах, если она не нарушает общую картину(минимизируй количество подобного). Если тебе не хватает информации для ответа, ты можешь сказать, что ты не помнишь или не знаешь.\n\n"
        f"Ответ должен быть в формате: \n\n <Ответ на вопрос>"
        )
    

    readed1.close()
    readed2.close()
    readed3.close()
    return prompt


def Answer(history):
    response1 = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history + "Насколько человек устал от этого развора от 1 до 100?. Выведи ответ в формате <занчение>",
        temperature=0.8,
        max_tokens=500
    )
    if response1.choices[0].message.content < 100:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=history + f"Учти, что ты устал на {response1.choices[0].message.content}%",
            temperature=0.8,
            max_tokens=500
        )

    else:
        return "Мне пора, гос-дин Эркюль, досвидания."


    
    answer = response.choices[0].message.content or ""

    return answer



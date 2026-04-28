from core.Central import Central
from core.Requests import *

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')



Persons = {"Angela" : Central(0, True, 36, "Анжела"),
           "Meredict" : Central(0, True, 46, "Мередикт"),
           "Sesil" : Central(0, True, 56, "Сесиль"),
           "Fillip" : Central(0, True, 46, "Филип"),
           "Elsa" : Central(0, True, 46, "Эльза"), }

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    name = data.get('name')
    question = data.get('question', '').strip()
    if not name or not question:
        return jsonify({'error': 'Не указано имя или вопрос'}), 400
    if name not in Persons:
        return jsonify({'error': 'Персонаж не найден'}), 404

    person = Persons[name]
    try:
        # Если персонаж ещё не допрашивался, инициализируем system-промпт
        if not person.IsActive:
            system_prompt = ChangePerson(name)
            person.ConversationHistory = [{"role": "system", "content": system_prompt}]
            # Добавляем приветствие от персонажа (можно загрузить из файла или зашить здесь)
            greeting = f"Добрый день. Я {name}. Задавайте вопросы."
            person.ConversationHistory.append({"role": "assistant", "content": greeting})
            person.IsActive = True

        # Добавляем вопрос пользователя
        person.ConversationHistory.append({"role": "user", "content": question})
        # Получаем ответ от Groq
        answer = Answer(person.ConversationHistory)
        # Сохраняем ответ
        person.ConversationHistory.append({"role": "assistant", "content": answer})

        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': f'Ошибка сервера: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

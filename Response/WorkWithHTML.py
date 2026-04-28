from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from core.Requests import ChangePerson, Answer

app = Flask(__name__)
CORS(app)  # разрешаем запросы с фронтенда

@app.route('/')
def index():
    return render_template('index.html')  # ваша HTML-игра

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    suspect_name = data.get('name')           # имя персонажа
    user_question = data.get('question')      # текущий вопрос
    history = data.get('history', [])         # история сообщений: [{"role": "user/assistant", "content": "..."}]
    
    if not suspect_name or not user_question:
        return jsonify({"error": "Missing name or question"}), 400
    
    # 1. Получаем системный промпт для этого персонажа (его характер)
    system_prompt = ChangePerson(suspect_name)   # читает файл Docs/Имя - PRESS.txt
    
    # 2. Собираем полный список сообщений для Groq
    messages = [
        {"role": "system", "content": system_prompt},
        *history,                     # предыдущие сообщения (user + assistant)
        {"role": "user", "content": user_question}   # текущий вопрос
    ]
    
    # 3. Вызываем вашу функцию Answer (отправляет запрос в Groq)
    try:
        answer = Answer(messages)
        return jsonify({"answer": answer})
    except Exception as e:
        print("Ошибка при вызове Groq:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
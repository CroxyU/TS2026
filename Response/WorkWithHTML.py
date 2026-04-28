import sys
import os
# Добавляем путь к корневой папке TS2026
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Теперь импорты работают
from core.Central import Central
from core.Requests import *

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')


NAMES = {"Филип Блейк":"Fillip", "Мередит Блейк": "Meredict", "Эльза Гриер" : "Elsa", "Сесилия Уильямс": "Sesil", "Анджела Уоррен": "Angela", "Angela":"Angela", "Sesil":"Sesil", "Elsa": "Elsa" ,"Meredict":"Meredict","Fillip":"Fillip"} 
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
    if not NAMES[name] or not question:
        return jsonify({'error': 'Не указано имя или вопрос'}), 400
    if NAMES[name] not in Persons:
        return jsonify({'error': 'Персонаж не найден'}), 404

    person = Persons[name]
    
    try:
        if not person.IsActive:
            system_prompt = ChangePerson(NAMES[name], person=person)
            person.ConversationHistory = [{"role": "system", "content": system_prompt}]
            greeting = f"Добрый день. Я {name}. Задавайте вопросы."
            person.ConversationHistory.append({"role": "assistant", "content": greeting})
            person.IsActive = True

        person.ConversationHistory.append({"role": "user", "content": question})
       
        answer = Answer(person.ConversationHistory)
        
        person.ConversationHistory.append({"role": "assistant", "content": answer})
        history2 = person.ConversationHistory[1:]
        #Angr = Answer([{"role":"system", "content" : f"Ты на допросе. В любой момент ты можешь закончить разговор, если слишком устал. Сейчас ты устал на {person.Angry} из 100. Насколько следующий вопрос тебя утомляет? Оцени полученный уровень усталости от 10 до 100. Когда усталость достигнет 100, разговор будет завершен. Для оценки принимай во внимание какие темы обсуждаются  (Если игрок пытается говорить о темах, не имеющих отношения к допросу, пытается сломать 'четвёртую стену' сильно повышай усталость ). Формат ответа: целое число без дополнительных символов."},person.ConversationHistory[-2]])
        Angr = Fatigue(history2, person)
        print(Angr)
        person.Angry += int(Angr)  
        data.set("Angry", person.Angry)
        print(f"Текущий уровень злости {name}: {person.Angry}")


        if person.Angry >= 100:
            person.IsActive = False
            ##
            print(f"Текущий уровень злости {name}: {person.Angry}")

        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': f'Ошибка сервера: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

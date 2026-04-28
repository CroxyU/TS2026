from core.Central import Central
from core.Requests import *
from Response.Main import *

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #ANSWER = Work(request.args.get("Name", default=None, type=None, ),request.args.get("Qestion", default=None, type=None, ))
    return render_template('hello.html', )



Persons = {"Angela" : Central(0, True, 36, "Анжела"),
           "Meredict" : Central(0, True, 46, "Мередикт"),
           "Sesil" : Central(0, True, 56, "Сесиль"),
           "Fillip" : Central(0, True, 46, "Филип"),
           "Elsa" : Central(0, True, 46, "Эльза"), }


if __name__ == '__main__':
    app.run(debug=True)

from core.Central import Central
from Response.WorkWithHTML import Persons
from core.Requests import Answer
from core.Requests import ChangePerson

def Work(Name, Question):
    P = Persons[Name]
    if P.IsActive:
        P.ConversationHistory.append({"role": "user", "content": Question})
        Ans = Answer(P.ConversationHistory)
        P.ConversationHistory.append({"role": "assistant", "content": Ans})

    else:
            P.ConversationHistory.append({"role": "system", "content": ChangePerson(Name)})
            P.ConversationHistory.append({"role": "user", "content": Question})
            Ans = Answer(P.ConversationHistory)
            P.ConversationHistory.append({"role": "assistant", "content": Ans})
            
    return Ans 
    
print(Work("Elsa", "Не помните ли вы, что вы делали в тот день?"))
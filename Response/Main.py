from core.Central import Central
from Response.WorkWithHTML import Persons
from core.Requests import Answer
from core.Requests import ChangePerson

def Work(Name, Quetion):
    Persons[Name].ConversationHistory.append(Quetion)
    if Persons[Name].IsActive:
        Ans = Answer(Persons[Name].ConversationHistory)
        Persons[Name].ConversationHistory.append(Ans)
        
    elif not Persons[Name].IsActive:
            Persons[Name].ConversationHistory.append(ChangePerson(Name))
            Ans = Answer(Persons[Name].ConversationHistory)
            Persons[Name].ConversationHistory.append(Ans)
    return Ans 
    

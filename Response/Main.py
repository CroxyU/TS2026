from core.Central import Central
from Response.WorkWithHTML import Persons
from core.Requests import Answer
from core.Requests import ChangePerson

def Work(Name, Quetion):
    P = Persons[Name]
    P.ConversationHistory.append(Quetion)
    if P.IsActive:
        Ans = Answer(P.ConversationHistory)
        P.ConversationHistory.append(Ans)
        
    elif not P.IsActive:
            P.ConversationHistory.append(ChangePerson(Name))
            Ans = Answer(P.ConversationHistory)
            P.ConversationHistory.append(Ans)
    return Ans 
    

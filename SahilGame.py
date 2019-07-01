print("Welcome to the game. Whenever you are choosing an option, please type in the exact choice")
class Choice:
    description = ""
    destination = ""

    def __init__(self, desc:str, dest:str):
        self.description = desc 
        self.destination = dest

class Decisionpoint:
    description = ""
    choices = []
   
    def __init__(self, d:str, c:[]):
        self.description=d
        self.choices=c

dictionary = {
    "start": Decisionpoint( "Where will you go?",  [
        Choice("Go to houston", "houston"),
        Choice("Or go to el paso", "el paso")  
    ] ),
    "houston": Decisionpoint("What Will You do?", [
        Choice("talk to stranger","talk to stranger"),
        Choice("Or talk to police?","talk to police")
    ] ),
    "talk to police": Decisionpoint("police arrest you",[
    ] ),
    "talk to stranger": Decisionpoint("Stranger gives you a horse, Where will you go?", [
        Choice("go north","north"),
        Choice("go south", "south")
    ] ),
    "south": Decisionpoint("While going south, you get hit by a train", [
       
    ] ),
    "north": Decisionpoint("After going north for 2 days, where will you go?", [
        Choice("go east","east"),
        Choice("go west", "west") 
    ] ),
    "east": Decisionpoint("While going east, you get robbed and shot by bandits", [
        
    ]),
    "west": Decisionpoint("After searching for 5 days, you finally found the treasure!", [
    ]),   
    "el paso": Decisionpoint("What Will You do?", [
        Choice("talk to person","talk to person"),
        Choice("Or go shopping?","go shopping")  
    ]),   
    "talk to person": Decisionpoint("person robs you and kills you", [
       
    ]),    
    "go shopping": Decisionpoint("What Will You buy?", [
        Choice("buy clothes","buy clothes"),
        Choice("or buy food?","buy food")
    ]),    
    "buy clothes": Decisionpoint("Stranger aproaches you and kills you for your clothes", [

    ]),
     "buy food": Decisionpoint("You find a stranger, what do you do?", [
        Choice("give him Food", "give him food"),
        Choice("or keep your food","keep your food")
    ]),
    "keep your food": Decisionpoint("Stranger gets mad and kills you", [
    ]),
    "give him food": Decisionpoint("Stranger likes you and asks you to come home with him, what do you do?", [
        Choice("go home","go home"),
        Choice("or don't go home", "don't go home")
    ]),
    "don't go home": Decisionpoint("Stranger gets mad and kills you", [
    ]),
    "go home": Decisionpoint("At the strangers house, you find a mysterious item. what do you do?", [
        Choice("leave", "leave"),
        Choice("Or steal the item", "steal the item")
    ]),  
     "leave": Decisionpoint("Stranger gets mad and kills you", [
    ]),
    "steal the item": Decisionpoint("The stranger doesn't notice you stealing his item, what do you do?", [
        Choice("leave", "leave"),
        Choice("or stay","stay")
    ]),    
    "leave": Decisionpoint("Stranger gets mad and kills you", [
    ]),
    "stay": Decisionpoint("The stranger goes to the bathroom, what do you do?", [
        Choice("leave", "leave"),
        Choice("or use the mysterious item","use the mysterious item")
    ]),   
    "leave": Decisionpoint("Stranger gets mad and kills you", [
    ]),
     "use the mysterious item": Decisionpoint("The mysterious item kills you", [
    ])
    }     

currently = dictionary["start"] 

while True:
    print(currently.description)

    if len(currently.choices) == 0:
        exit()
    
    for ch in currently.choices:
        print(ch.description)
    
    p = input()

    n = True 
    for ch in currently.choices:
        if p == ch.destination:
            n = False
            currently = dictionary[p]
            break
    
    if n:
        print("Please choose a choice")

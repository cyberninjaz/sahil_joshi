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
    "start": Decisionpoint( "WHERE WILL YOU GO?",  [
        Choice("Go to Houston", "Houston"),
        Choice("Or Go to El Paso", "El Paso")  
    ] ),
    "Houston": Decisionpoint("What Will You do?", [
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
    "El Paso": Decisionpoint("What Will You do?", [
        Choice("talk to person","talk to person"),
        Choice("Or Go shopping?","go shopping")  
    ]),   
    "talk to person": Decisionpoint("person robs you and kills you", [
       
    ]),    
    "go shopping": Decisionpoint("What Will You buy?", [
        Choice("Buy Clothes","buy clothes"),
        Choice("or Buy Food?","buy food")
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

import random as r
from objects import fruits

Tries = 10

Word = r.choice(fruits)  

List =[]


for i in range(len(Word)):
    List += "_"
    
print(List)

game = True

while game:
    
    Guess = input("Please enter a letter to guess: ")

    for x in range(len(Word)):
    
        letter = Word[x]
    
        if letter == Guess:
            List[x] = Guess
    
    print(List)
    
    if Guess not in Word:
        Tries -= 1
        
        if Tries == 0:
            game = False
            print("You are a noob.")
            
    if "_" not in List:
        game = False
        print("You are the chosen one.")        





    



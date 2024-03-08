import random as r

Lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
List = []



def easy_pass(length_pass):
    
    for a in range(length_pass):
        Lower = r.choice(Lower_case)
        List.append(Lower)
            
    for b in range(length_pass):
        Upper = r.choice(Upper_case)
        List.append(Upper)

    for c in List:
        r.shuffle(List)
        print(c, end="")


def medium_pass(length_pass):
    
    for a in range(length_pass):
        Lower = r.choice(Lower_case)
        List.append(Lower)
    
    for b in range(length_pass):
        Upper = r.choice(Upper_case)
        List.append(Upper)
    
    for c in range(length_pass):
        Number = r.choice(Numbers)
        List.append(Number)
        
    for d in List:
        r.shuffle(List)
        print(d, end="")


def hard_pass(length_pass):
    
    for a in range(length_pass):
        Lower = r.choice(Lower_case)
        List.append(Lower)
        
    for b in range(length_pass):
        Upper = r.choice(Upper_case)
        List.append(Upper)
        
    for c in range(length_pass):
        Number = r.choice(Numbers)
        List.append(Number)
        
    for d in range(length_pass):
        Symbol = r.choice(Symbols)
        List.append(Symbol)
        
    for e in List:
        r.shuffle(List)
        print(e, end="")
        

running = True

while running:
    
    Option = input("What level of password do you wanna generate, Easy, Medium or Hard: ")
    Input = Option.lower()
    
    Length = int(input("Please enter the length of the password you wanna generate: "))
    
    if Input == "easy":
        easy_pass(Length)
        running = False
    
    elif Input == "medium":
        medium_pass(Length)
        running = False
        
    elif Input == "hard":
        hard_pass(Length)
        running = False
        
    else:
        print("Please enter one of the following options!")
    
        
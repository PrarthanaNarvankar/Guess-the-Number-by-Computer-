import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Enter the number between 1 to {x}:" ))
        if guess < random_number:
            print("Sorry...guess again.Its too low")
        elif guess >random_number:
            print("Sorry....guess again.Its too high")
            
    print(f"Congrats! You have guess the number {random_number} correctly")         
                        
guess(20)        
    

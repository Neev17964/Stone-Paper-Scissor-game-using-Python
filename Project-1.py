user = input("Choose between stone, paper or scissor: ")   # Getting input from the user

import random
random_number = random.randint(1,3)   # Random Number Generator

user_dict = {"stone" : 1,
             "paper" : 2,
             "scissor" : 3}   # Defining user input as values 

user_number = user_dict[user]  #  Taking the user input and converting as 1 or 2 or 3

if(random_number == 1 and user_number == 1):
    print("SYSTEM: STONE")
    print("OOPS TIE!!")

elif(random_number == 1 and user_number == 2):
    print("SYSTEM : STONE")
    print("HURRAY YOU WON!!!!")    

elif(random_number == 1 and user_number == 3):
    print("SYSTEM : STONE")
    print("OOPS YOU LOST \nTRY AGAIN") 


elif(random_number == 2 and user_number == 1):
    print("SYSTEM: PAPER")
    print("OOPS YOU LOST \nTRY AGAIN")

elif(random_number == 2 and user_number == 2):
    print("SYSTEM : PAPER")
    print("OOPS TIE!!")

elif(random_number == 2 and user_number == 3):
    print("SYSTEM : PAPER")
    print("HURRAY YOU WON!!!!")      


elif(random_number == 3 and user_number == 1):
    print("SYSTEM : SCISSOR")
    print("HURRAY YOU WON!!!!") 

elif(random_number == 3 and user_number == 2):
    print("SYSTEM : SCISSOR")
    print("OOPS YOU LOST \nTRY AGAIN") 

elif(random_number == 3 and user_number == 3):
    print("SYSTEM : SCISSOR")
    print("OOPS TIE!!")        

else:
    print("Something Went Wrong.....")
#  If-ELif-Else Ladder to get the different scenarios
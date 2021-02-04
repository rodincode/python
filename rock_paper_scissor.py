# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:11:49 2019

@author: LENOVO
"""

import random
name=input('your name: ')

def add_greeting(name):
    
    greeting="hello "+ name
    return greeting

text=add_greeting(name)
print(text)
    
print('paper=1')
print('rock=2')
print('scissor=3')


def play_again():
    command=input('enter S to start the New game and Q to quit the game ')
    computerScore=0
    userScore=0
    command=command.lower()
   
    if command=='s':
        no_of_rounds=int(input('no. of rounds'))
        while no_of_rounds not in range(3,11): 
            print("enter between 3 to 11")
            no_of_rounds=int(input('no. of rounds'))
#           if (no_of_rounds>=3) and (no_of_rounds<=10):
        for r in range(1,no_of_rounds+1):
                            userMove=int(input('enter your move: '))
                            computerMove=random.randint(1,3) 
                            print('computer move: ',computerMove)
                            if userMove in range(1,4):
                                if (userMove==computerMove):
                                    print('tie')
                                    userScore=userScore
                                    computerScore=computerScore
                                    print('userScore= ',userScore)
                                    print('computerScore= ', computerScore)
                                elif ((userMove==1) and (computerMove==2)) or ((userMove==2) and (computerMove==3)) or ((userMove==3) and (computerMove==1)):
                                    print('you win')
                                    userScore=userScore+1
                                    print('userscore=', userScore)
                                else:
                                    print('you loose')
                                    computerScore=computerScore+1
                                    print('computerscore= ', computerScore)
                            else:
                                print('enter no. between 1 to 3')
                                r=r-1
                                
    elif command=='q':
        print("quit")
    else:
        print('Please enter S or Q')
            
play_again()
command = input(' Press s to go back to game or q to quit').lower()
while(command!='q'):
    if command == "s":
        play_again()
    elif command == "q":
        print("END")
        break;
    else:
        print("Invalid command. Please try again")
        command = input('enter S to start the new game and Q to quit the game ').lower()
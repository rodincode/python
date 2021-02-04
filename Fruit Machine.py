# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:54:50 2019

@author: LENOVO


The player starts with Rs. 10 credit, with each go costing Rs. 2. 
If the Fruit Machine “rolls” two of the same symbol, the user wins Rs. 2.
 The player wins Rs. 10 for three of the same and Rs. 50 for 3 Bells.
 The player loses Rs. 1 if two skulls are rolled and all of his/her money if
 three skulls are rolled. The player can choose to quit with the winnings after
 each roll or keep playing until there is no money left.
 
"""
print("##############################")
print("#                            #")
print("#      | Fruit Machine |     #")
print("#       | By Rohan |      #")
print("#                            #")
print("##############################")
print("")

while True:
    import random
    credit = 10
 
    wheel = ['Cherry', 'Lemon', 'Bell', 'Star', 'Skull']
 
    reel1 = random.choice(wheel)
    reel2 = random.choice(wheel)
    reel3 = random.choice(wheel)
 
    start = input("Enter Roll or Quit? ")
     
    if start == "quit" or start == "Quit":
      print("Your winnings are Rs." + str(credit))
      break
     
    if start == "roll" or start == "Roll":
      credit = (credit - 2)
      print("- Rs. 2")
      print("Credit now Rs." + str(credit))
      print()
      print("\n ***  Spinning Wheels... *** \n")
      print()
      print(reel1 + " - " + reel2 + " - " + reel3 + "\n")
      print()
       
      if start != "quit" and start != "roll":
        continue
 
      credit = (round(credit, 2))
       
      if credit < 0:
        print(" Sorry Unable to play no credits")
        break
       
      if reel1 == "Skull" and reel2 =="Skull" and reel3 == "Skull":
        print(" You lost all your money! :-(")
        credit = (credit - credit)
 
      if reel1 == "Skull" == reel2 =="Skull" or reel2 == "Skull" == reel3 =="Skull" or reel1 == "Skull" == reel3 =="Skull":
        print(" You lost Rs.1!\n")
        credit = (credit - 1)
 
      if reel1 == reel2 or reel2 == reel3 or reel1 == reel3: 
        print(" $-$ Rs.20 Won $-$\n")
        credit = (credit + 50)
   
      if reel1 == reel2 == reel3:
        print(" $$$ Rs.10 Won $$$\n")
        credit = (credit + 10)
   
      if reel1 == "Bell" == reel2 == "Bell" == reel3 == "Bell":
        print(" $$$ Rs.50 won $$$ ")
        credit = (credit + 50)
 
      credit = (round(credit, 2))
 
      print("Credit now Rs." + str(credit))



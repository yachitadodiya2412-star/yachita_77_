#rock,paper and scissors game

import random

choice=("rock","paper","sissors")
computer=random.choice(choice)
player=input("choose rock,paper,scissor")
print("computer choose:",computer)
if player==computer:
    print(" it's a tie!!!")
elif(player=="rock"and computer=="scissors") or\
    (player=="paper"and computer=="rock") or\
    (player=="scissors"and computer=="paper"):
    print("you win!!!")
else:
    print("computer win!!!")

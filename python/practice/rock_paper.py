#!/usr/bin/python3

while True:
    p1ch=input("Rock , Paper or Scissors?")
    p2ch=input("Rock , Paper or Scissors?")
    if((p1ch=="Rock"and p2ch=="Scissors") or (p1ch=="Scissors"and p2ch=="Paper")
    or (p1ch=="Paper"and p2ch=="Rock")):
        print("Player 1 wins")
    elif((p2ch=="Rock"and p1ch=="Scissors") or (p2ch=="Scissors"and p1ch=="Paper")
    or (p2ch=="Paper"and p1ch=="Rock")):
        print("Player 2 wins")
    else:
        print("Plese enter a valid input")
    ch=input("Do you wish to play again? Please enter Yes or No")
    if(ch=="No"):
        break
    else:
        continue

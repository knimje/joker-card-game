#IF PLAYER A AND PLAYER B ARE PLAYINF WITH NUMBERS SIMULTANEOUSLY AND BOTH SHOULD ENTER DIFFERENT NUMBER let a set a game over number 
score1,score2,game=0,0,1
a=int(input("enter JOKER for PLAYER 1 between 4 to 7 "))
b=int(input("enter JOKER for PLAYER 2 between 4 to 7 "))
print("\n")
print("the game has started ")
print("NUMBERS TO BE ENTERED BETWEEN 10 TO 49 ")
from time import sleep

for second in range(3,0,-1):
  print(second)
  sleep(1)
print("Go")
print("\n")
while game !=0:
    c=int(input(" player 1 "))
    if c%b!=0 and c!=(a*b):
        score1+=1
    if c%b==0:
        score1+=0
    if  c==(a*b): 
        print("GAME OVER")
        game=0
        break
    d=int(input(" player 2 "))
    if d%a!=0 and d!=(a*b):
        score2+=1
    if d%a==0:
        score2+=0
    if  d==(a*b): 
        print("GAME OVER")
        game=0
        break
print(f"Score of PLAYER 1 IS {score1} \n Score of Player 2 is {score2}")
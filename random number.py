import random 
import math
print("                           WELCOME")
print("                              TO")
print("                   NUMBER GUESSING GAME")
print("      ----------- Instructions and Rules----------")
print("1.You will be given 5 chances to guess the correct number")
print("2.For correct guess you will earn 1 point and lose for wrong guess")
print("3.MAXIMUM SCORE:5 ")
print("4.MINIMUM SCORE:0")
print("5.Press enter to play the game")
print()
print()
print("Input the Upper And Lower bound according to you.")
print()
lower_bound = int(input("Enter the lower bound of the range : "))
print()
upper_bound = int(input("Enter the upper bound of the range : "))
generated_number = random.randint(lower_bound,upper_bound)
score=5
i=1
while i<=5:
    print()
    guessed=int(input("Enter the number between "+ str(lower_bound)+" and "+ str(upper_bound)+": "))
    i=i+1
    if guessed==generated_number** :
              print()
              print("****Congratulations,you have won!!!****")
              print("Your Guess is Correct and You have taken attempts for the right answer.")
              print("***YOUR FINAL SCORE:"+str(score)+"****")
              break
    elif(guessed>generated_number ):
              print()
              print("Guessed number is greater than generated number")
              score=score-1
              print("Sorry,Try another chance!")

    elif(guessed<generated_number ):
              print()
              print("Guessed number is lesser than generated number")
              score=score-1
              print("Sorry,Try another chance!**")

    
if(score==0) :
    print()
    print("Your chances hace been exhausted.")
    print("OOPS!!!YOU LOSE THE GAME")
    score=score-1
    print("**SCOREBOARD**")
    print()
    print("***YOUR FINAL SCORE:-  "+str(score)+"****")

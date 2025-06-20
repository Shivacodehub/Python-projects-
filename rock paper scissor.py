import random
user= int(input("enter the desired value :\n 👉 0 for rock 🪨 \n 👉 1 for paper 🗞️ \n 👉 2 for scissor ✂️  "))
val=random.randint(0,3)
print("Bot selected")
if val==0:
    print("🪨")
if val==1:
    print("🗞️")
if val==2 :
    print("✂️")
          
if user not in range(0,2):
    print("Please choose the value between 0,1,2")
else:
 if val == user:
    print("It is Draw")
 elif (val==0 and user==2):
    print("You lose the game")
 elif (val==2 and user==0):
    print("You won the game")
 elif (val>user):
    print("You lose the game") 
 elif (val<user):
    print("You won the game")        

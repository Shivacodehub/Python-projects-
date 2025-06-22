import random
import string
password=""
char=int(input("How many alphabets you prefer in password"))
num=int(input("How many numbers you prefer in password"))
sym=int(input("How many symbols you prefer in password"))
for i in range(char):
    alpha=random.choice(string.ascii_letters)
    password+=alpha
#print(password)
for i in range(0,num):
    numb=random.randint(0,9)    
    password+=str(numb)
symbols = string.punctuation    
for i in range(sym) :   
    symb= random.choice(symbols) # Get 5 random symbol
    password+=''.join(symb) # Join them into a string
print("weak password :",password)
passwords=list(password)
random.shuffle(passwords)
passwords=''.join(passwords)
print("strong password:",passwords)

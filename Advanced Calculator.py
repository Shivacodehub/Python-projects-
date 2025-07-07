import math
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def addition(first_num,second_num):
    return first_num+second_num

def substraction(first_num,second_num):
    return first_num-second_num
def multiplication(first_num,second_num):
    return first_num*second_num
def division(first_num,second_num):
    return first_num/second_num
def modulus(first_num,second_num):
    return first_num%second_num
def power(first_num,second_num):
    return pow(first_num,second_num)   
def squareroot(a):
    return math.sqrt(a)
def sine(radian):
    return math.sin(radian)            
def cosine(radian):
    return math.cos(radian)   
def tangent(radian):
    return  math.tan(radian) 
def radian_conv(degree) :
    return math.radians(degree)   

print("=======================================")
print("     ADVANCED SCIENTIFIC CALCULATOR    ")
print("=======================================")
print("Choose an operation:\n"
 "1. Addition (+)\n"
 "2. Subtraction (-)\n"
 "3. Multiplication (*)\n"
 "4. Division (/)\n"
 "5. Modulus (%)\n"
 "6. Power (x^y)\n"
 "7. Square Root (√x)\n"
 "8. Sine (sin x)\n"
 "9. Cosine (cos x)\n"
 "10. Tangent (tan x)\n")
while True:
    choice = int(input("Enter your choice (1–10): "))
    if choice == 1:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        result = addition(first_num=first_number, second_num=second_number)
        print("------------------------------")
        print("Result= ", first_number, "+", second_number, "=", result)
        print("------------------------------")
    elif choice == 2:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        result = substraction(first_num=first_number, second_num=second_number)
        print("------------------------------")
        print("Result= ", first_number, "-", second_number, "=", result)
        print("------------------------------")
    elif choice == 3:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        result = multiplication(first_num=first_number, second_num=second_number)
        print("------------------------------")
        print("Result= ", first_number, "*", second_number, "=", result)
        print("------------------------------")
    elif choice == 4:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        if second_number==0:
            print("Invalid input a number can not be divisible by zero,pl enter correct input")
            second_number = int(input("Enter the second number: "))
            result = division(first_num=first_number, second_num=second_number)
            print("------------------------------")
            print("Result= ", first_number, "/", second_number, "=", result)
            print("------------------------------")
            
        else:    
            result = division(first_num=first_number, second_num=second_number)
            print("------------------------------")
            print("Result= ", first_number, "/", second_number, "=", result)
            print("------------------------------")
    elif choice == 5:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        if second_number==0:
            print("Invalid input a number can not be divisible by zero")
            second_number = int(input("Enter the second number: "))
            result = modulus(first_num=first_number, second_num=second_number)
            print("------------------------------")
            print("Result= ", first_number, "%", second_number, "=", result)
            print("------------------------------")
        else:    
            result = modulus(first_num=first_number, second_num=second_number)
            print("------------------------------")
            print("Result= ", first_number, "%", second_number, "=", result)
            print("------------------------------")
    elif choice == 6:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        result = power(first_num=first_number, second_num=second_number)
        print("------------------------------")
        print("Result= ", first_number, "^", second_number, "=", result)
        print("------------------------------")
    elif choice == 7:
        first_number = int(input("Enter the number: "))
        result = squareroot(first_number)
        print("------------------------------")
        print("Result= √", first_number, "=", result)
        print("------------------------------")
    elif choice == 8:
        option = int(input("If you want to enter degree type 1 or radian type 2 : "))
        if option == 1:
            value = int(input("Enter the degree : "))
            result = sine(radian_conv(value))
        elif option == 2:
            value = int(input("Enter the radian : "))
            result = sine(value)
        print("------------------------------")
        print("Result= sin(", value, ")=", result)
        print("------------------------------")
    elif choice == 9:
        option = int(input("If you want to enter degree type 1 or radian type 2 : "))
        if option == 1:
            value = int(input("Enter the degree : "))
            result = cosine(radian_conv(value))
        elif option == 2:
            value = int(input("Enter the radian : "))
            result = cosine(value)
        print("------------------------------")
        print("Result= cosine(", value, ")=", result)
        print("------------------------------")
        
    elif choice == 10:
        option = int(input("If you want to enter degree type 1 or radian type 2 : "))
        if option == 1:
            value = int(input("Enter the degree : "))
            result = tangent(radian_conv(value))
        elif option == 2:
            value = int(input("Enter the radian : "))
            result = tangent(value)
        print("------------------------------")
        print("Result= tangent(", value, ")=", result)
        print("------------------------------")
        
    new_cal = input("Do you want to perform another calculation? (yes/no): ")
    if new_cal.lower() =="yes":
        clear = input("Do you want to clear the screen? (yes/no): ")
        if clear.lower() =="yes":
            clear_screen()
            print("Choose an operation:\n"
            "1. Addition (+)\n"
            "2. Subtraction (-)\n"
            "3. Multiplication (*)\n"
            "4. Division (/)\n"
            "5. Modulus (%)\n"
            "6. Power (x^y)\n"
            "7. Square Root (√x)\n"
            "8. Sine (sin x)\n"
            "9. Cosine (cos x)\n"
            "10. Tangent (tan x)\n")
        else:
            pass    
    else:
        break

print("=======================================")
print("Thank you for using the calculator!")
print("======================================")
    
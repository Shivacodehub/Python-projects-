import os

print("********* WELCOME TO SILENT AUCTION PROGRAM *********")

bidders = {}

while True:
    name = input("What is your name? ")
    
    try:
        bid = int(input("What is your bid? ₹"))
    except ValueError:
        print("Invalid bid. Please enter a number.")
        continue
    
    bidders[name] = bid
    more_bidders = input("Are there any other bidders? Enter 'yes' or 'no': ").lower()
    
    if more_bidders == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        break

highest_bid = 0
winner = ""

for bidder, amount in bidders.items():
    if amount > highest_bid:
        highest_bid = amount
        winner = bidder

print(f"The winner is {winner} with a bid of ₹{highest_bid}")
from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

name = input("What is your name? ")
bid_amount = input("How much will you bid?: $")
try:
    bid_amount = int(bid_amount)
except ValueError:
    bid_amount = float(bid_amount)
end_of_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ")
clear()

bidders = {}
bidders[name] = bid_amount

while end_of_bidding == 'yes':
    name = input("What is your name? ")
    bid_amount = input("How much will you bid?: $")
    try:
        bid_amount = int(bid_amount)
    except ValueError:
        bid_amount = float(bid_amount)
    bidders[name] = bid_amount
    end_of_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ")
    clear()

highest_bid = 0
winner_bidder = ""
for name, bid_amount in bidders.items():
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner_bidder = name
      
if end_of_bidding == 'no':
  print(f"The winner is {winner_bidder} with a bid of ${highest_bid}.")

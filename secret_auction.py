# Secret Auction Program
# This program collects bids from multiple users and determines the highest bidder.

bids = {}

def auction():
    name = input("What is your name: ")
    price = int(input("What is your bid $: "))
    bids[name] = price

def highest(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print("The winner of this auction is", winner, "with highest bid of $", highest_bid)

more = True

auction()

while more:
    others = input("Are there any other bidders? Type yes or no: ").lower()

    if others == "yes":
        print("\n" * 50)
        auction()
    else:
        more = False
        highest(bids)
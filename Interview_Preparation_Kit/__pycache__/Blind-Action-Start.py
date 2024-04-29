import os
def bidInfo():
    bid_dict = {}
    i = 1
    while i > 0:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        bid_dict[name] = bid
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

        if more_bidders == "yes":
            
            def findHighestBid(bid_dict):
                highest_bid = 0
                for bidder in bid_dict:
                    bid_amount = bid_dict[bidder]
                    if bid_amount > highest_bid:
                        highest_bid = bid_amount
                        winner = bidder
                return f"Winner is {winner} with the highest bid {highest_bid}$"
        else:
            i -= 1
    print(findHighestBid(bid_dict))
    return bid_dict

bidInfo()

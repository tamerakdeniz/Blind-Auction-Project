import art
print(art.logo)
bid_for_person = {}
# TODO-1: Ask the user for input ++

decision = True
while decision:
    person = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

# TODO-2: Save data into dictionary {name: price} ++

    bid_for_person[person] = bid

# TODO-3: Whether if new bids need to be added ++

    decision = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 20)
    if decision == "no":
        decision = False

# TODO-4: Compare bids in dictionary

winner = max(bid_for_person, key=bid_for_person.get)

print(f"The winner is {winner} with a bid of {bid_for_person[winner]}")
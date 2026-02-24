MAX_TICKETS = 5
tickets_sold = 0


while tickets_sold <= MAX_TICKETS:
    name = input("Name? ")

    # Exit code break
    if name == "xxx":
        break

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all of the tickets (ie: {MAX_TICKETS} tickets).")

else:
    print(f"Sorry but you tried to buy {tickets_sold} but there are only {MAX_TICKETS} left.")












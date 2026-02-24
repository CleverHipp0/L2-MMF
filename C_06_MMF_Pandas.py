import pandas


# Set up lists for user details
all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharges,
}

# Cool format
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Total'] - 5

total_paid = sum(mini_movie_frame['Total'])
total_profit = sum(mini_movie_frame['Profit'])

print(mini_movie_frame)
print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")


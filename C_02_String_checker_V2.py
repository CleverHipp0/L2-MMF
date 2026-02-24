# Functions go here.
def statement_generator(statement, decoration):
    """Makes a simple statement look nice by adding a decoration to the beginning and end."""
    print(f"{decoration * 3} {statement} {decoration * 3}")

def string_checker(question, valid_answers=("yes", "no"), first_letter_count=1):
    """Asks a yes or no question and requires a yes or no response."""

    # Repeats asking until it is answered appropriately with "yes" or "no".
    while True:
        result = input(question).lower().strip(r"\ ")

        for item in valid_answers:
            # If the result is in tolerable answers then return the first letter of the response.
            if result == item or result == item[:first_letter_count]:
                return item


        # Error message for iff a mistake is made.
        print(f"🚨 ERROR: This Field is required. Please enter a response from this list: {valid_answers}. 🚨")


# Main routine goes here.

# Asks the user if they want instructions.
instructions = string_checker("Would you like to read the instructions? ")
print(f"You choose {instructions}.")

if instructions == "yes":
    # Instructions.
    statement_generator("instructions", "ℹ️")
    print('''
How to fall down stairs:
    Step 1:
    Step 2:
    Step 4:
    Step 8:
    Step 16:
    ''')

payment_types = ("cash", "credit")
payment_method = string_checker("How would you like to pay (cash or credit)? ", payment_types, 2)
if payment_method == "credit":
    pass
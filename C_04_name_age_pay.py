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
            if result == item or result[:first_letter_count] == item[:first_letter_count]:
                return item


        # Error message for iff a mistake is made.
        print(f"🚨 ERROR: This Field is required. Please enter a response from this list: {valid_answers}. 🚨")

def not_blank(inquiry):
    """Checks whether an answer is not blank."""

    # This repeats the inquiry until it is answered
    while True:
        element = input(inquiry)

        # Checks the length of the answer and outputs an error if it is too short.
        if len(element.strip()) > 0:
            return element
        else:
            print("🚨 ERROR: This Field is required. Please enter a response. 🚨")

def int_checker(question):
    """Checks if a number is an integer"""

    # Error message set up
    error = "🚨 ERROR: Please enter an integer (whole number) more than zero. 🚨"

    while True:
        # Strips unnecessary character
        result = input(question).strip(r"\ ")

        # Checks if the number is an integer and then outputs an error if it isn't
        try:
            result = int(result)
            return result

        except ValueError:
            print(error)


# Main routine goes here.
# Asks the user if they want instructions.
instructions = string_checker("Would you like to read the instructions? ")
print(f"You choose {instructions}.\n")

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

# Loop For testing.
while True:

    # Ask for name.
    name = not_blank("Name: ")

    # Asks for age.
    age = int_checker("Age: ")

    # Checks if they are old enough.
    if age > 122:
        print("Sorry you are too old.\n")
        continue

    elif age < 12:
        print("Sorry you are too young. You need to be over 12.\n")
        continue

    else:
        pass

    # Ask for payment type.
    payment_type = string_checker("Payment type (cash/credit): ", ("cash", "credit"), 2)

    print(f"Thank you {name} for ordering a ticket using {payment_type}!")
    print()
















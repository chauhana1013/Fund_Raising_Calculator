# Checks that user has enteres yes / no to a question
def yes_no(question):

    to_check = ["yes", "no"]

    while True:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        print("Please enter either yes or no...\n")

# Main Routine...
print()
print("💸💸💸 Welcome to The Fund Raising Calculator 💸💸💸")
print()

show_instructions = yes_no("Would you like to view the instructions? ")

if show_instructions == "yes":
    print("📜📜📜 Instructions 📜📜📜")
    print()
    print("This program will ask you for...")
    print("- The name of the product you are selling")
    print("- How many items you plan on selling")
    print("- The costs for each component of the product")
    print("- How much money you want to make")
    print()
    print("It will then output an itemised list of the costs with subtotals for the variable and ficed costs.")
    print("Finally it will tell you how much you should sell each item for to reach your profit goal.")
    print()
    print("The data will also be written to a text file which has the same name as your product.")
    print()

print("🟢🟢🟢 PROGRAM LAUNCHED 🟢🟢🟢")
print()

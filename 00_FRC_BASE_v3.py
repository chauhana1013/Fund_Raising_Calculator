import pandas
import math

# Functions Here...

# Checks that input is either a float or an integer that is more than zero. Takes in custom errors
def num_check(question, error, num_type): 
    while True:

        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError: 
            print(error)

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

# Checks that input was not blank, if blank, then the program outputs error message
def not_blank(question, error):
    while True:
        response = input(question)

        # If user's response is blank, program displays this message
        if response == "":
            print(f"{error}. \nPlease try again.\n")
            continue
       
        return response

# Currency Formatting Function
def currency(x):
    return f"${x:.2f}"

# Gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):

    # Set up dictionaries and lists
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":
        
        print()
        # Get Item, Quantity, and Price
        item_name = not_blank("Item Name: ", "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break
        
        if var_fixed == "variable":
            quantity = num_check("Quantity: ", "The amount must be a whole number more than zero.", int)
        else:
            quantity = 1

        price = num_check("How much? $", "The price must be a number <more than 0>", float)

        # Add Item, Quantity, and Price
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find Sub Total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currenncy function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

# Prints Expense Frames
def expense_print(heading, frame, subtotal):
    print()
    print(f"***** {heading} Costs *****")
    print(frame)
    print()
    print(f"{heading} Costs: ${subtotal:.2f}")
    return ""

# Takes User's Total Cost and Outputs Profit Goal needed to be achieved
def profit_goal(total_costs):
    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    while True:
        
        # Ask for Profit Goal...
        response = input("What is your profit goal (eg $500 or 50%) ")

        # Check if first character is $...
        if response [0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # Check if last character is %
        elif response [-1] == "%":
            profit_type = "%"
            # Get amount (everything befor the %)
            amount = response[:-1]

        else:
            # Set response to amount for now
            profit_type = "unknown"
            amount = response
        
        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        
        except ValueError:
            print(error)
            continue
        
        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars? , y / n")

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(f"Do you mean {amount}%? , y / n")

            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"
        
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal

# Rounding Function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# Main Routine Here...
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


# Get Product Name
product_name = not_blank("Product Name: ", "The product name can't be blank")

how_many = num_check("How many items will you be producing? ", "The number of items must be a whole number more than zero", int)


print()
print("Please enter your variable costs below...")
# Get Variable Costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y/n)? ")

if have_fixed == "yes":
    # Get Fixed Costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0

# Work out Total Costs and Profit Target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculate Total Sales Needed to reach Goal
sales_needed = all_costs + profit_target

# List for Write to File


# Ask User for Rounding
round_to = num_check("Round to nearest...? $", "Can't be 0", int)

# Calculate Recommended Price
selling_price = sales_needed / how_many
print(f"Selling Price (unrounded): ${selling_price:.2f}")

recommended_price = round_up(selling_price, round_to)
print(f"Recommended Price: ${recommended_price:.2f}")

# Text string for printing / writing to file
frc_heading = f"***** Fund Raising - {product_name} *****"

variable_heading = f"***** Variable Costs *****"
variable_txt = pandas.DataFrame.to_string(variable_frame)
variable_sub_txt = f"Variable Costs Subtotal: ${variable_sub:.2f}"

sales_heading = f"***** Sales Advise *****"
required_sales = f"Sales Needed: ${sales_needed:.2f}"
profit_target_txt = f"Profit Target: ${profit_target:.2f}"
minimum_price_txt = f"Minimum Price: ${selling_price:.2f}"
recommended_price_txt = f"Recommended Price: ${recommended_price:.2f}"

if have_fixed == "yes":
    fixed_heading = f"***** Fixed Costs *****"
    fixed_txt = pandas.DataFrame.to_string(fixed_frame)
    fixed_sub_txt = f"Fixed Costs Subtotal: ${fixed_sub:.2f}"
    
    to_write = [frc_heading, variable_heading, variable_txt, variable_sub_txt, fixed_heading, fixed_txt, fixed_sub_txt, sales_heading, profit_target_txt, required_sales, minimum_price_txt, recommended_price_txt]
    
else:
    fixed_heading = f"***** No Fixed Costs *****"

    to_write = [frc_heading, variable_heading, variable_txt, variable_sub_txt, fixed_heading, sales_heading, profit_target_txt, required_sales, minimum_price_txt, recommended_price_txt]


# Printing Area

# Write to file...
# Creat file to hold data (add .txt extension)
file_name = f"{product_name}.txt"
text_file = open(file_name, "w+")

for item in to_write:
    print(item)
    print()
# Heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# Close File
text_file.close()


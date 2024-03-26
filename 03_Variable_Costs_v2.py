import pandas

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

        quantity = num_check("Quantity: ", "The amount must be a whole number more than zero.", int)

        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)

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


# Main Routine Here...

# Get Product Name
product_name = not_blank("Product Name: ", "The product name can't be blank")

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Printing Area

print()
print(variable_frame)
print()

import math

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

# Rounding Function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to


# Main Routine...
how_many = num_check("How many items? ", "Can't be 0", int)
total = num_check("Total Costs? ", "More than 0", float)
profit_goal = num_check("Profit Goal? ", "More than 0", float)
round_to = num_check("Round to nearest...? ", "Can't be 0", int)

sales_needed = total + profit_goal

print(f"Total: ${total:.2f}")
print(f"Profit Goal: ${profit_goal:.2f}")

selling_price = sales_needed / how_many
print(f"Selling Price (unrounded): ${selling_price:.2f}")

recommended_price = round_up(selling_price, round_to)
print(f"Recommended Price: ${recommended_price:.2f}")
# Functions...

# Checks users enter an integer to a given question
def num_check(question): 
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError: 
            print("Please enter an integer (i.e. a number which does not have a decimal part)")

# Main Routine...

print()
while True:

    number = num_check("Integer: ")

    if number > 0:
        print("Program Continues") 
    
    else:
        print("Please enter a integer that is more than 0")
        continue
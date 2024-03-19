# Functions Here...

# Checks users enter an integer to a given question
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


# Main Routine Here...
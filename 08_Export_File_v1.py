import pandas

# Frames and Content for Export
variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"], 
    "Quantity": [300, 300, 50],
    "Price": [1, .5, .75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork" , "Advertising"],
    "Price": [25, 35, 10]
}

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recommended_price = "$5.00"

print(variable_frame)

# Change Dataframe to String (so it can be written to a txt file)
variable_txt = pandas.DataFrame.to_string(variable_frame)

# Write to file...
# Creat file to hold data (add .txt extension)
file_name = f"{product_name}.txt"
text_file = open(file_name, "w+")

# Heading
text_file.write(f"***** Fund Raising - {product_name} *****\n\n")
text_file.write(variable_txt)



# Close File
text_file.close()
"""
This script can be used to build filters through Code Editor of a Domain Definitionin Odoo v12.

This script transforms a one-column csv file of items into a text file inclusive List .
The line of code can then be copied-pasted in the code section

Editor: Jonathan Verschaeve
"""

import os
from tkinter import filedialog
from csv import reader

print("Script is launched. \nWARNING: csv file should be one column.")

#User selects a field name to build Product Domain Filter. By default, it will be 'code_prefix'
field_name = input("Select a field name to buil the filter on:\n 1- for 'code_prefix'\n 2- for 'email'\n 3- for 'name'\n Or type a valid field name: \n").lower()

def field_name_code(linecode):
    if linecode == "1":
        return "code_prefix"

    elif linecode == "2":
        return "email"

    elif linecode == "3":
        return "name"

    else:
        return linecode

field_name = field_name_code(field_name)

print("The code editor will be build on: ",field_name)

#Script points to csv file
print("Please select a csv file from the opening file directory window.")

file_path = filedialog.askopenfilename()
parent_path = os.path.dirname(file_path)

#Function to load and read csv file
def load_csv(filename):
    data = list()
    with open(filename,"r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            data.append(*row)
        return data

list_elements = load_csv(file_path)

#Create a text file to write converted code
with open(r"file_converted.txt", "w") as file_conversion:

    #Write opening character
    file_conversion.write('[["' + field_name +'", in, [')

    #Write code for elements in csv file, except the last element
    for ele in list_elements[0:-1]:
        file_conversion.write('"' + ele + '",')

    #Write code for the last element only
    last_ele = list_elements.pop()
    file_conversion.write('"' + last_ele + '"]')

    #Write closing characters
    file_conversion.write(']]')

file_conversion.close()

print("A text file will open automatically with the conversion code.\nPlease find the text file here: ", parent_path)
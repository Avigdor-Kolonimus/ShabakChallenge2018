# ***********************************************************************************
# The program fix WhoAmI.jpg from Shabak Challenge 2018 in Software and Data Science
# Autor Alexey Titov
# Version 1.0
# Data 12.2018
# ***********************************************************************************

# library
import json

# open and create files
jpg_file = open("WhoAmI.jpg", mode='r', encoding="UTF-8")
json_file = open("newWhoAmI.json", mode="w", encoding="UTF-8")

#
for line in jpg_file:
    newline = line.replace('"value": ?','"value": "?"')
    json_file.write(newline)
# closing
jpg_file.close()
json_file.close()
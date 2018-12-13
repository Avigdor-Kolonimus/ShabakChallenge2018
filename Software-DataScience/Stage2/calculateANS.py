# ***********************************************************************************
# The program calculate answer for Shabak Challenge 2018 in Software and Data Science 
# Autor Alexey Titov
# Version 1.0
# Data 12.2018
# ***********************************************************************************

# libraries
import json
import statistics
import base64

# hebrew gematria https://en.wikipedia.org/wiki/Gematria
HebrewGematria = {
            'u05D0': 1, 'u05D1': 2, 'u05D2': 3, 'u05D3': 4, 'u05D4': 5, 'u05D5': 6, 'u05D6': 7, 'u05D7': 8, 'u05D8': 9,
			'u05D9': 10, 'u05DB': 20, 'u05DC': 30, 'u05DE': 40, 'u05E0': 50, 'u05E1': 60, 'u05E2': 70, 'u05E4':	80, 'u05E6': 90,
			'u05E7': 100, 'u05E8': 200, 'u05E9': 300, 'u05EA': 400
}

jsonfile = open("newWhoAmI.json", mode='r', encoding='latin_1')
jsondata = json.load(jsonfile)      # load whole file as JSON

list_of_values = [] # will store here all values we found

for key in jsondata.keys():       # start moving key one by one
    for line_of_text in jsondata[key]: 
        tmp_str = str(line_of_text)   		# convent json to string
        total = 0                       	# sum of gematria for this key
        for hebrew_unicode in HebrewGematria.keys():                	# check every unicode in the string
            counter = tmp_str.count(hebrew_unicode.lower())   		# count number of appearance
            total = total + (counter * HebrewGematria[hebrew_unicode])  # summorize
        list_of_values.append(total)

# calculate median
MEDIAN = statistics.median(list_of_values) 
sum_of_values_below_median = 0    # initialization for final answer
for i in list_of_values:
    if i < MEDIAN:
        sum_of_values_below_median = sum_of_values_below_median + i    # final sum of values below median

# print answer
answer = str(sum_of_values_below_median)
print("Answer in Base64: ")
print(base64.b64encode(answer.encode()))

# closing
jsonfile.close()

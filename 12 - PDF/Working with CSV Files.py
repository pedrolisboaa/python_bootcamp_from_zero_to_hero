import csv

# Open the file
data = open('example.csv', encoding='utf-8')
# csv.reader
csv_data = csv.reader(data)
# format it into a python object list of lists
data_lines = list(csv_data)

print(data_lines)
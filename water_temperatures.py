import csv

with open('water_temp.txt', 'r') as csv_file:
    reader = csv.reader(csv_file)
    temperatures = list(reader)

# temperatures = [print("{:<5} {:<15} {:<10}\n".format(item[0], item[5] + ": ", int((((float(item[4]) * 9)/5) + 32))) +
#                 "\u00b0 F") for item in temperatures if item[4] != 'Water Temp']
input_set = []

for item in temperatures:
    input_set = [item[5], item[1]]

headers = ["Date", "Wave Height"]

wave_height = {}
wave_height[0] = input_set[1]
wave_height[1] = input_set[0]
wave_height = {header: input_set[index] for index, header in enumerate(headers)}

# end = {header: input_set[index] for index, header in enumerate(headers)}
# print(list(enumerate(headers)))
print(wave_height)

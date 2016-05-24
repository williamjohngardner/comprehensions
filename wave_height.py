# def wave_height():

from csv_parse import csv_parse

temperatures = csv_parse()

dates = [item[5] for item in temperatures]
del dates[0]
heights = [item[1] for item in temperatures]
del heights[0]


dictionary = dict(zip(dates, heights))
# dictionary = {}
# for index, date in enumerate(dates):
#     for height in heights:
#         dictionary[dates] = height

# nested_dictionary = {date: [height[index] for height in heights] for index, date in enumerate(dates)}

my_list = []
for index, value in dates.items():
    my_list.append(value)
print(my_list)

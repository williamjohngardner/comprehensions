# def daily_averages():

import datetime
from wave_height import wave_height
from collections import defaultdict

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

dictionary = wave_height()

# print(dictionary)

nested_dictionary = {}

for key, value in dictionary.items():
    day_index = datetime.datetime.strptime(key, "%Y-%m-%d").weekday()
    nested_dictionary = [days[day_index], value]
    # print(nested_dictionary)

avg_dictionary = defaultdict()

for key, value in nested_dictionary:
    avg_dictionary[key].append(value)
    print(avg_dictionary)



# dates = {value for value in dictionary.items()}
# for each value in a dictionary, return the 'value' at the iterable index.
# print(dates)
# dates_string = ' '.join(dates)
# print(dates_string)



# return average

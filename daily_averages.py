# def daily_averages():

from csv_parse import csv_parse
from wave_height import wave_height

temperatures = csv_parse()

dates = [item[5] for item in temperatures]
heights = [item[1] for item in temperatures]

del dates[0]
print(len(dates))
del heights[0]

for i in heights:
    float_heights = map(float(i), i)
    # float_heights = map(float, i)
    print(sum(float_heights))

# [print("{:<5}\n".format(float(sum(i))/len(dates))) for i in heights if i != 'Water Temp']
# average = [print(float(sum(i[2]))) for i in heights]


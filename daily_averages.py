# def daily_averages():

import datetime
from wave_height import wave_height
from day_conversion import get_day_of_week

dictionary = wave_height()

dates = [value for value in dictionary]
# for each value in a dictionary, return the 'value' at the iterable index.
dates_string = ' '.join(dates)
# print(dates_string)

days = []
def get_dow(date_string):
    return days[datetime.datetime.strptime(dates_string, "%Y-%m-%d").weekday()]

print([get_dow(dates_string) for day in days])


# return average

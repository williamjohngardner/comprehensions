def wave_height():

    from csv_parse import csv_parse

    temperatures = csv_parse()

    dates = [item[5] for item in temperatures]
    del dates[0]
    heights = [item[1] for item in temperatures]
    del heights[0]

    # dictionary = dict(zip(dates, heights))

    nested_dictionary = {value: heights[index] for index, value in enumerate(dates)}
    # for each index and value pair in an enumerated list of dates, return 'value' as a key and the value of "heights"
    # at the iterable index.

    return nested_dictionary

def wave_height():

    from csv_parse import csv_parse

    temperatures = csv_parse()

    dates = [item[5] for item in temperatures]
    heights = [item[1] for item in temperatures]

    dictionary = dict(zip(dates, heights))

    return dictionary

def water_temp():

    from csv_parse import csv_parse

    temperatures = csv_parse()

    temperatures = [print("{:<5} {:<15} {:<10}\n".format(item[0], item[5] + ": ", int((((float(item[4]) * 9)/5) +
                        32))) + "\u00b0 F") for item in temperatures if item[4] != 'Water Temp']

    return temperatures

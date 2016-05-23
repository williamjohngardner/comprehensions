def csv_parse():

    import csv

    with open('water_temp.txt', 'r') as csv_file:
        reader = csv.reader(csv_file)
        temperatures = list(reader)

    return temperatures

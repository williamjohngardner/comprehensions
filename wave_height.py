def wave_height():

    from csv_parse import csv_parse

    temperatures = csv_parse()

    input_set = []

    for item in temperatures:
        input_set = [item[5], item[1]]

    headers = ["Date", "Wave Height"]

    wave_height = {}
    wave_height["Date"] = input_set[0]
    wave_height["Wave Height"] = input_set[1]
    wave_height = {header: input_set[index] for index, header in enumerate(headers)}

    wave_height_list = [list(wave_height.values()) for items in wave_height]
    return wave_height_list

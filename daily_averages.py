def daily_averages():

    import datetime
    from wave_height import wave_height
    from collections import defaultdict

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    dictionary = wave_height()

    nested_list = []

    for key, value in dictionary.items():
        day_index = datetime.datetime.strptime(key, "%Y-%m-%d").weekday()
        nested_list = [days[day_index], value]

    avg_dictionary = defaultdict(list)

    avg_dictionary = [day_index.append(float(height)) for day, height in nested_list.items()]
    print(avg_dictionary)


    return average

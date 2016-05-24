def daily_averages():

    from csv_parse import csv_parse
    from wave_height import wave_height

    temperatures = csv_parse()

    dates = [item[5] for item in temperatures]
    heights = [item[1] for item in temperatures]

    del dates[0]
    # print(len(dates))
    del heights[0]

    float_heights = [float(i) for i in heights]
    sum_float_heights = sum(float_heights)
    average = sum_float_heights/len(dates)

    return average

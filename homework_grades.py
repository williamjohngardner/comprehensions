def homework_grades():

    from statistics import mean

    dictionary = {'Gale': {'Homework 1': 88, 'Homework 2': 76}, 'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                  'Peyton': {'Homework 1': 84, 'Homework 2': 77}, 'River': {'Homework 1': 85, 'Homework 2': 91}}

    grades = []

    # for key, value in dictionary.items():
    #     grades.append(value['Homework 1'])

    # average = mean(grades)

    average = mean([value['Homework 1'] for key, value in dictionary.items()])

    return average

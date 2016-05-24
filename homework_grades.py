def homework_grades():

    dictionary = {'Gale': {'Homework 1': 88, 'Homework 2': 76}, 'Jordan': {'Homework 1': 92, 'Homework 2': 87}, 'Peyton': {'Homework 1': 84, 'Homework 2': 77}, 'River': {'Homework 1': 85, 'Homework 2': 91}}

    grades = []

    for key in dictionary.values():
        for index in key.values():
            grades.append(index)

    return sum(grades)/8
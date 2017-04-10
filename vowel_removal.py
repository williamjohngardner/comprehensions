def vowel_removal():

    sentence = "List Comprehensions are the Greatest!"
    vowels = 'aeiouAEIOU'

    end = [letter for letter in sentence if letter not in vowels]
    end = ''.join(end)
    print(end)

vowel_removal()

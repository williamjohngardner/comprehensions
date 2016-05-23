sentence = "List Comprehensions are the Greatest!"
vowels = 'aeiouAEIOU'

# for vowel in vowels:
#     sentence = sentence.replace(vowel, "")

end = [letter for letter in sentence if letter not in vowels]

end = ''.join(end)

print(end)

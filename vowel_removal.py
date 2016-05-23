
sentence = ("List Comprehensions are the Greatest!").lower()
vowels = 'aeiou'


for i in vowels:
    sentence = sentence.replace(i, "")

#no_vowels = [letter.replace(vowels, "") for letter in sentence]

print(sentence)

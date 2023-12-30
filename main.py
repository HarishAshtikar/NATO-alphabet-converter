import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("Enter Word: ")
result = [dict[letter.upper()] for letter in word]
print(result)

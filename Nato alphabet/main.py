import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Enter thew word: ").upper()
output_list = [phonetic_dic[letter] for letter in word]

print(output_list)

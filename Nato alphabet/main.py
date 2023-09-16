import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dic)


def generate_phonetic():
    word = input("Enter thew word: ").upper()

    try:
        output_list = [phonetic_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please!!")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()

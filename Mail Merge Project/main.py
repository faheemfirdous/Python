PLACEHOLDER = "[name]"

with open("C:/Users/fahee/PycharmProjects/Mail+Merge+Project+Start/inputs/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("../MAIL+MERGE+PROJECT+START/letter/letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        s_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, s_name)

        with open(f"../Mail+Merge+Project+Start/outputs/letter_for_{s_name}.txt", mode="w") as c_letter:
            c_letter.write(new_letter)

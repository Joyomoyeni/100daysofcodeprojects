import pandas
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
is_correct = True
while is_correct:
    user = (input("Enter your word:")).upper()
    try:
        nato_user = [nato_dict[n] for n in user]
        print(nato_user)
        is_correct = False
    except KeyError:
        print("Sorry, only letters in the alphabet please")


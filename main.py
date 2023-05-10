import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = pandas.DataFrame(data)

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
#print(nato_dict)


def generate_nato_dict():
    user_data = input("what is the word you want? ").upper()

    try:
        user_nato_dict = [nato_dict[alphabet] for alphabet in user_data]
    except KeyError:
        print("sorry only letters in the alphabet please \n")
        generate_nato_dict()
    else:
        print(user_nato_dict)
        game_is_on = False


generate_nato_dict()

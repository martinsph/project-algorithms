def aux(string):
    letter_dict = {}
    for letter in string.lower():
        if letter in letter_dict:
            # this increment does not add a key, but updates an existing one 
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
        # print(letter_dict)
    return letter_dict


def is_anagram(first_string, second_string):
    # check if strings are empty
    if first_string == "" or second_string == "":
        return False

    # to make the code faster it checks is the letter lenght are not equal
    if len(first_string) != len(second_string):
        return False

    # calls aux function to create dicts to comparison
    first_dict = aux(first_string)
    second_dict = aux(second_string)

    # if both are equals then, return true, otherwise, false
    return first_dict == second_dict

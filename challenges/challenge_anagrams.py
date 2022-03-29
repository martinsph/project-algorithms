def aux(string):
    letter_dict = {}
    for letter in string.lower():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False

    if len(first_string) != len(second_string):
        return False

    first_dict = aux(first_string)
    second_dict = aux(second_string)

    return first_dict == second_dict

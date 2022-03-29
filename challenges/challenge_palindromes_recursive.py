def is_palindrome_recursive(word, low_index, high_index):
    # check if word is a empty string
    if word == "":
        return False

    if len(word) <= 1:
        return True

    if high_index < low_index:
        return True

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return False

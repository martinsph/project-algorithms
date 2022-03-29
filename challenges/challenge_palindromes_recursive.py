def is_palindrome_recursive(word, low_index, high_index):
    # check if word is a empty string
    if word == "":
        return False

    # One letter words are considered palindromes
    if len(word) <= 1:
        return True

    # when the higher index is less than the lower the word is over.
    # If it has not crashed yet its because is a palindrome.
    if high_index < low_index:
        return True

    # check if letters are equal and use recursion
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return False

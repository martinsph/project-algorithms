def is_palindrome_iterative(word):
    # check if word is a empty string
    if word == "":
        return False

    # One letter words are considered palindromes
    if len(word) <= 1:
        return True

    if word == "".join(reversed(word)):
        return True

    return False

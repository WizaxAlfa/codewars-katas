def alphabet_position(text):
    import string
    alphabetPosition = ""
    for character in text.lower().replace(' ', ''):
        if character not in (string.punctuation + string.digits):
            alphabetPosition += str(string.ascii_lowercase.index(character) + 1) + ' '
    return alphabetPosition.rstrip()


alphabet_position ("abduscan")
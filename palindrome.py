def permute_a_palindrome(input): 
    impares = 0
    for char in set(input):
        input.count(char)
        if char % 2 != 0:
            impares += 1
    return impares > 1
permute_a_palindrome("aaa")

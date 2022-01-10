def palindrome(word, index):
    return f'{word} is a palindrome' if word == word[::-1] else f'{word} is not a palindrome'


# ----------------------------(2)-------------
# def palindrome(word , index):
#     reversed_word = ''.join(list(reversed(word)))
#     if word == reversed_word:
#         return f'{word} is a palindrome'
#     else:
#         return f'{word} is not a palindrome'


'''
print(palindrome('abcba', 0))
-------------------

abcba is a palindrome
'''
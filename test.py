# 1. Design a function that reverses the digits of an integer.
# For example, 50 should become 5 and -12 should become -21.
def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n *= sign
    reversed_n = int(str(n)[::-1])
    return sign * reversed_n

n = 70
print(reverse_integer(n)) 


# 2. Write a recursive function to calculate the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = 4
print(factorial(n))


# 3. Design a function that takes a string or sequence of characters as input
# and returns the character that appears most frequently.
# For example, '11189' => '1' and 'hello' => 'l'
def most_frequent_char(s):
    from collections import Counter
    count = Counter(s)
    return max(count, key=count.get)

s = 'Entepreneur'
print(most_frequent_char(s))


# 4. Design a function that determines whether a given string is a pangram.
# A pangram is a sentence or phrase containing every letter of the alphabet at least once.
# Punctuation and case are typically ignored.
def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

s = 'The quick brown fox jumps over the lazy dog'
print(is_pangram(s))


# 5. Design a function that takes a list of integers as input.
# The function should return True if the list contains two consecutive threes (3 next to a 3)
# anywhere within the list. Otherwise, it should return False.
# For example, the function should return True for [1, 3, 3] and False for [1, 3, 1, 3].
def has_consecutive_threes(lst):
    for i in range(len(lst) - 1):
        if lst[i] == 3 and lst[i + 1] == 3:
            return True
    return False

lst = [1, 3, 1, 3]
print(has_consecutive_threes(lst))



# 6. Design a function that takes a sentence as input and returns a new sentence with the words
# reversed in the same order that Master Yoda would use.
def yoda_speak(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

sentence = 'Reject finance bill'
print(yoda_speak(sentence))

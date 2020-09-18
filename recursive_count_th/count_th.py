'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    n = "th"
    # n1 = len(word)
    # n2 = len(n)
    
    if len(word) < len(n):
        return 0
    if word == n:
        return 1
    if (word[0 : len(n)] == n):
        return count_th(word[len(n) - 1:]) + 1
    
    return count_th(word[len(n) - 1:])
    
    
# print(count_th("thethe"))

# word = "thhtthht"
# print(word[1:])
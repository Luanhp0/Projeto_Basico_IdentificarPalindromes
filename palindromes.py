import math

def is_palindrome(word):
    J = len(word)-1
    result = 0
    for i in range(len(word)):
        if word[i] == word [J]:
            result = result + 1
        if i >= J:    
            break
        J = J - 1    

    if result == math.ceil(len(word)/2):
        return True
    else:
        return False

    def is_palindrome_recursive(word):
        if len(word) <= 1:
            return True
        else:
            return word[0] == word[-1]    




words = ["arara", "racecar", "carro", "cama", "level"]

for word in words:
    print(word)
    print(is_palindrome(word))
    print("\n")
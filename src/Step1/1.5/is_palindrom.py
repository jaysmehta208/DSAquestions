def is_palindrome(string, index):
    if (index >= len(string)/2):
        return "True"
    if (string[index] != string[len(string) - 1 - index]):
        return "False"
    return is_palindrome(string, index+1)
print(is_palindrome("alsla", 0))
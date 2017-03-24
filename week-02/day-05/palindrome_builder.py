w = input("Tell me a word so I can create a palindrome! - ")
def create_palindrome(w):
    w = w + w[::-1]
    return w
print(create_palindrome(w))

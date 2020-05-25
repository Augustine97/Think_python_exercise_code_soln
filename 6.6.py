"""Exercise 6.6.A palindrome is a word that is spelled the same backward and forward, like “noon”
and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the
middle is a palindrome. """

def is_palindrome(word):
    if word==word[::-1]:
        print('True')
    else:
        print('False')

if __name__=='__main__':
    word=input()
    is_palindrome(word)
    
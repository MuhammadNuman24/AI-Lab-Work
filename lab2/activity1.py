word2=input("enter a word: ")
def isPalindrome(word):
    temp=word[::-1]
    if temp.capitalize()==word.capitalize():
         return True
    else:
        return False
print(isPalindrome(word2))

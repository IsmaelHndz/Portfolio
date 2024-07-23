def palindrome (word):
    if word [::] == word[::-1]:
        print("Is palindrome")
    else:
        print("Is not palindrome")

if __name__ == "__main__":
    palindrome("none")

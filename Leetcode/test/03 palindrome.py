def solution(inputString):
    inputString = inputString.replace(' ', '').lower()
    if inputString[::] == inputString[::-1]:
        return True
    else:
        return False



https://app.testdome.com/screening/test/d4ce56561348413ba9ace8da7bfb8129
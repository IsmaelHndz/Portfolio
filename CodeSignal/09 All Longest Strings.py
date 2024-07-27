#Given an array of strings, return another array containing all of its longest strings.

def solution(inputArray):
    longest = []
    newArray = []
    for i in inputArray:
        if len(i) > len(longest):
            longest = i
    for i in inputArray:
        if len(i) == len(longest):
                    newArray.append(i)
    
    print(newArray)
    return newArray

if __name__ == '__main__':
    print(solution(["asd", "asdf", "as", "cd", "cddf", "cddfdf", "kms", "kmv", "akjs", "vkje"]))
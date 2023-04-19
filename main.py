
def commonCharacters(strings):
    if len(strings) == 0:
        return []

    shortStrIndex = findShortestIndex(strings)
    shortString = strings[shortStrIndex]

    commonChars = []

    for i in range(len(shortString)):
        if inAll(shortString[i], strings):
            if shortString[i] not in commonChars:
                commonChars.append(shortString[i])
    return commonChars
#-----------------------------------------------------------------
def inAll(ch, stringsList):
    for j in range(len(stringsList)):
        if ch not in stringsList[j]:
            return False
    return True
#-----------------------------------------------------------------

def findShortestIndex(stringsList):
    index = 0
    shortLen = len(stringsList[0])

    for i in range(1, len(stringsList) - 1):
        if len(stringsList[i]) < shortLen:
            shortLen = len(stringsList[i])
            index = i
    return index


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(commonCharacters(["abc", "bcd", "cbaccd"]))
    print(commonCharacters(["a", "d", "cbaccd"]))
    print(commonCharacters(["abcde", "bcd", "b"]))
    if "apple" in ["apple", "banana"]: print ("yes")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def makeUpper(word):
    return word.upper()

words = ["Python","Functions","Bhavika","Mapping", "Filters"]
result = map(makeUpper,words)

print(list(result))

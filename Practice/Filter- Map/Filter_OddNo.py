def isOdd(a):
    return a%2 !=0

numbers = [1,2,3,4,5,6,7,8,9,10]
result = filter(isOdd , numbers)
print(list(result))

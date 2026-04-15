def isAdult(user):
    return user["age"] >=18

users = [
    {"name" : "Bhavika", "age" : 21},
    {"name" : "Aancahl", "age" : 21},
    {"name" : "Diya" ,"age" : 23},
    {"name" : "Niky", "age" : 19},
    ]

result = filter(isAdult,users)
print(list(result))

people = [
    {"first" : "Bhavika", "last" : "Sonule"},
    {"first" : "Aanchal", "last" : "Jayswal"},
    {"first" : "Diya", "last" : "Goriya"},
    {"first" : "Nikita", "last" : "Sonule"}
    ]

names = []
for p in people:
    full=p["first"] + " " + p["last"]
    names.append(full)
print(names)

def isLongEmail(email):
    return len(email) > 15

emails = ["nikysonule@gmail.com","bhavikasonule@gmail"]
result = filter(isLongEmail, emails)
print(list(result))

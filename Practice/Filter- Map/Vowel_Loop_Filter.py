words = ["apple","banana","cat","dog","eagle","ice","orange"]

vowelWord=[]

for w in words:
    if w.startswith(("a","e","i","o","u")):
        vowelWord.append(w)
print (vowelWord)

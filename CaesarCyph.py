caesarString = input("Enter the cypher: ")

stringList = list(caesarString)

print(str(stringList))
string1 = ""
l = 0
for l in range(len(stringList)):
        decryptDig = ord(stringList[l]) - 3 
        string1 += chr(decryptDig)

print(string1)

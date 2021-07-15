n=int(input("number of dict pairs: "))
inputDict={}
for i in range(n):
    stringTemp=input()
    inputDict[stringTemp.split(":")[0]]=stringTemp.split(":")[1]
for key,value in inputDict.items():
    inputDict[value]=key
    del inputDict[key]
print(inputDict)
    
fileTypes=input('String for file types:')
n=int(input('number of files: '))
fileNames=[]
for i in range(n):
    fileNames.append(input())
tempList=list(fileTypes.split(";"))
typeDict={}
for i in tempList:
    strSplit=i.split(",")
    typeDict[strSplit[0]]=strSplit[1]
ansDict={}
for i in fileNames:
    ansDict[i]="unknown"
    if "." in i and i.split(".")[1] in typeDict:
        ansDict[i]=typeDict[i.split(".")[1]]
print(ansDict)
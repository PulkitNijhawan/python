n=int(input("number of dicts: "))
inputList=[]
for i in range(n):
    dictString=input()
    tempList=dictString.split(',') #fruit:orange,color:orange
    tempDict={}
    for j in tempList:
        tempDict[j.split(':')[0]]=j.split(':')[1]
    inputList.append(tempDict)
key=input("keyword: ")
def mySort(dict):
    return dict[key]
inputList.sort(key=mySort)
print(inputList)
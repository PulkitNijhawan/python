n=int(input("number of elements: "))
inputList=[]
for i in range(n):
    inputList.append(int(input()))
start=int(input())
end=int(input())
x=inputList[start:end+1:2]
print(x)
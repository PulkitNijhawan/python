# print("plukit","hi",end='fi')
# print(":nextline")
# num=int(input('type number: '))
# print(num//5)
# x=3
# y=4
# first= x==y
# second= x<y
# print(not(first or second))
# x=input("name: ")
# if x=='pulkit':
#     print("hi")
# else:
#     print('bye')
# x=[4,"pulkit",True,1.2]
# x.append(1)
# print(x,len(x))
# x=range(10)
# for i in x:
#     print(i)
# x=[1,2,3,4,5]
# sliced=x[4:2:-1]
# print(sliced)
# y=[1,2,3,4,55,4]
# x=set(y)
# print(x)
# name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
# roll_no = [ 4, 1, 3, 2 ]
# marks = [ 40, 50, 60, 70 ]
# mapped=list(zip(name,roll_no,marks))
# print(mapped)
import functools
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = functools.reduce(lambda x,y: x+y, [10,23, -45, 33])
A8 = list(map(lambda x: x*2, [1,2,3,4]))
A9 = filter(lambda x: len(x) >3, ["I" , "want", "to", "learn", "python"])
print(A0)
# Input: 
# Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
# must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

# f(mainstream, must_watch) should return:

# ["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note", "One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]

n1=int(input("number of first list items: "))
n2=int(input("number of second list items: "))
mainstream=[]
must_watch=[]
for i in range(n1):
    mainstream.append(input())
for i in range(n2):
    must_watch.append(input())
temp1=set(mainstream)
temp2=set(must_watch)
print(list(temp1&temp2),",",list(temp1^temp2))
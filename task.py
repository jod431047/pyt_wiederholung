# dict  erstellen

info = {
    "name":"jihad",
    "age":33,
    "country":"Germany",
    "work":"Developer"
}
print(info.keys())
print(info.values())
print(info.get("work"))
thisdict=dict(x=[1,2,3,4,5],y=[1,22,33,33],k=[100,150,334])
print(thisdict)

#calculater
y = int(input("Bitte erste zahl geben"))
x = int(input("Bitte erste zahl geben"))
print(x+y)
print(x*y)
print(x/y)
print(x-y)

#List
nameList=["jihad","bayan","karam",1,2,3,4]
print(nameList)
print(nameList[2])
print(nameList[-1])

string
x = [1,2,3,4,5,6,7]
y = [111,22,33,44,55,55]
print(x)
print(x,y)
x.append(8)
print(x)
y.append(66)
print(y)
x.insert(9,100)
print(x)
x.extend(y)
print(x)
x.sort(reverse=True)
print(x)
x.remove(1)
print(x)
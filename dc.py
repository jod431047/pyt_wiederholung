# dict  erstellen
# info = {
#     "name":"jihad",
#     "age":33,
#     "country":"german"
# }
# print(info.keys())                       # dict_keys(['name', 'age', 'country'])
# print(info.values())                     # dict_values(['ziad', 27, 'german']) just the dict_values
# print(info.get("age"))                   # 27 ,when the key not found than using .get(key,"message") to user
# thisdict = dict(x=[2, 3, 4], y=[2, 3, 4], z=[2, 3, 4])
# print(thisdict)

info = {
    "name":"bari",
    "age":33,
    "countray":"syria",
    "work":"developer"
}

print(info.keys())
print(info.values())
print(info.get("work"))
thisdict = dict(x=[2,3,4,5],y=[5,6,7,8],j=[11,12,13,14])
print(thisdict)

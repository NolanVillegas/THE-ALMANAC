import json

with open('filename.json', 'r') as handle:
    mydict = json.load(handle)

function_input = input("Function: ")
mylist = function_input.split("|")
key = mylist[1].strip()
value = mylist[0].strip()

mydict[key] = value



with open('filename.json', 'w') as handle:
    json.dump(mydict, handle)



print(mydict)


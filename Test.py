import json

with open('filename.json', 'r') as handle:
    mydict = json.load(handle)

function_input = input("Function: ")
mylist = function_input.split("|")
value = mylist[0].strip()
key = mylist[1].strip()

mydict[value] = key



with open('filename.json', 'w') as handle:
    json.dump(mydict, handle, sort_keys=True, indent = 2)


# for value, key in mydict.items():
    print(f"Function inputted: {key}, Syntax inputted: {value}")



with open("my_list.txt", "w") as handle:
        handle.write("{:^200}  {:^125}\n".format("Function:","Syntax:\n"))
        for key, value in mydict.items():
             handle.write("{:^200}  {:^125}\n".format(value, key))
            
       
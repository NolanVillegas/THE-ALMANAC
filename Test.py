import json


print("\n\n\033[35mEnter a function and its syntax in format 'Function | Syntax'\nType \"deposit\" to save and deposit the input(s).\033[0m\n\n\n")


with open('filename.json', 'r') as handle:
        mydict = json.load(handle)

while True:
    
    function_input = input("\033[36mFunction|Syntax: \033[0m")
    mylist = function_input.split("|")

    if function_input.lower() == "deposit" :
         break

    if len(mylist) != 2:
        print("Invalid input. Please enter a valid function and syntax in the specified format.")
        continue

    value = mylist[0].strip()
    key = mylist[1].strip()
    mydict[value] = key

    print(f"Function inputted: {value}, Syntax inputted: {key}")

    sortdict = sorted(mydict.items(), key = lambda x: x[0])

    with open('filename.json', 'w') as handle:
        json.dump(mydict, handle, sort_keys=True, indent = 2)


    with open("my_list.txt", "w") as handle:
        handle.write("{:^80}  {:^100}\n".format("Function:","Syntax:\n"))
        for item in sortdict:
             handle.write("{:^80}  {:^100}\n".format(item[0], item[1]))
            
       
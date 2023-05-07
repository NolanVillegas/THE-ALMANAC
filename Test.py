import json



print("\n\n\033[35mEnter a function and its syntax in format 'Function | Syntax'\nType \"deposit\" to save and deposit the input(s).\033[0m\n\n\n")

def search(data, searcht):
    results = []
    for key, value in data.items():
         if searcht in key or searcht in value:
              results.append((key,value))
    return results

with open('filename.json', 'r') as handle:
        mydict = json.load(handle)
def find() :
    while True :
        find_spec = input("\033[92mFind: \033[0m")
        if find_spec.lower().strip() == "exit" : 
            break
        search_res = search(mydict, find_spec)
        print('\n')
        print(f"\033[35m\033[4mSearch Results for {find_spec}\033[0m")
        for key, value in search_res:
            print(f"\033[92m{key}:    {value}\033[0m")
        print('\n')

while True:
    
    function_input = input("\033[36m\033[1mFunction|Syntax: \033[0m")
    mylist = function_input.split("|")

    if function_input.lower().strip() == "deposit" :
         break
    
    if function_input.lower().strip() == "find" :
         print("\033[35mSearch for a term or type \'exit\' to exit\033[0m\n") 
         find()
         break

    if len(mylist) != 2:
        print("\033[31mInvalid input. Please enter a valid function and syntax in the specified format.\033[0m")
        continue

    value = mylist[0].strip()
    key = mylist[1].strip()
    mydict[value] = key

    print(f"\033[36mFunction inputted:\033[0m {value}\033[36m  Syntax inputted:\033[0m {key}")

    sortdict = sorted(mydict.items(), key = lambda x: x[0])

    with open('filename.json', 'w') as handle:
        json.dump(mydict, handle, sort_keys=True, indent = 2)


    with open("my_list.txt", "w") as handle:
        handle.write("{:^80}  {:^100}\n".format("Function:","Syntax:\n"))
        for item in sortdict:
             handle.write("{:^80}  {:^100}\n".format(item[0], item[1]))




       
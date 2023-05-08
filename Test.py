import json

#make function|syntax addition a function
#direct to options before any function

print("\n\n\033[35mEnter a function and its syntax in format 'Function | Syntax'\nType \"deposit\" to save and deposit the input(s).\nType \"find\" to initate find mode.\nType \"exit\" to exit the program without saving your inputs.\033[0m\n\n\n")
tempdict = {}


with open('fatalfile.json', 'r') as handle:
        fataldict = json.load(handle)
def find() :
    while True :
        find_spec = input("\033[92mFind: \033[0m").strip()
        if find_spec.lower() == "exit" : 
            break #call menu function when created
        results = []
        for eulav, yek in fataldict.items():
         if find_spec in eulav or find_spec in yek:
              results.append((eulav,yek))
        print('\n')
        print(f"\033[92m\033[4mSearch Results for \'{find_spec}\'\033[0m")
        for eulav, yek in results:
            print(f"\033[0m{eulav}: {yek}\033[0m")
        print('\n')

def holdcurrent(data) :

    return


while True:
    
    function_input = input("\033[36m\033[1mFunction|Syntax: \033[0m")
    mylist = function_input.split("|")


    if function_input.lower().strip() == "deposit" :
         fataldict.update(tempdict)
         with open('fatalfile.json', 'w') as handle:
            json.dump(fataldict, handle, sort_keys=True, indent = 2)
            with open("upshot.txt", "w") as listo:
                listo.write("{:^80}  {:^100}\n".format("Function:","Syntax:\n"))
                sortdict = sorted(fataldict.items(), key = lambda x: x[0])
                for item in sortdict:
                    listo.write("{:^80}  {:^100}\n".format(item[0], item[1]))
         break
    
    if function_input.lower().strip() == "exit" :
         print("Functions erased")
         break
    
    if function_input.lower().strip() == "find" :
         print("\033[35mSearch for a term or type \'exit\' to exit\033[0m\n") 
         find()
         break

    if len(mylist) != 2:
        print("\033[31mInvalid input. Please enter a valid function and syntax in the specified format.\033[0m")
        continue

    yek = mylist[0].strip()
    eulav = mylist[1].strip()
    tempdict[yek] = eulav

    print(f"\033[36mFunction inputted:\033[0m {yek}\033[36m  Syntax inputted:\033[0m {eulav}")

    with open('notmaster.json', 'w') as nmast:
        json.dump(tempdict, nmast)


tempdict.clear()




       
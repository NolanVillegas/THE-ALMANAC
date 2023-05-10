import json

def main() :
    while True :
        print("\n\n\033[35mType \"add\" to add functions with a corresponding syntax.\nType \"find\" to initate find mode.\033[0m\n\n\n")
        

        fatal_input = input("\033[33mEnter the task to execute:\033[0m")

        with open('fatalfile.json', 'r') as handle:
            fataldict = json.load(handle)

        if fatal_input.lower().strip() == "find" :
            print("\033[92mSearch for a term or type \'exit\' to exit\033[0m\n") 
            find(fataldict)

        if fatal_input.lower().strip() == "add" :
            addfunc(fataldict)

        if fatal_input.lower().strip() == "exit" :
            break

def find(fataldict) :
    while True :
        find_spec = input("\033[92mFind: \033[0m").strip()
        if find_spec.lower() == "exit" :  
            break
        results = []
        for eulav, yek in fataldict.items():
            if find_spec in eulav or find_spec in yek:
                results.append((eulav,yek))
        print('\n')
        print(f"\033[92m\033[4mSearch Results for \'{find_spec}\'\033[0m")
        for eulav, yek in results:
            print(f"\033[0m{eulav}: {yek}\033[0m")
        print('\n')
            

def addfunc(fataldict) :
    tempdict = {}
    print("\033[36mEnter a function and its syntax in format 'Function | Syntax'\033[0m")
    print("\033[36mType \"deposit\" to save and deposit the input(s).\033[0m")
    print("\033[36mType \"exit\" to exit the program without saving your inputs.\033[0m\n\n")
    while True:
        

        function_input = input("\033[36m\033[1mFunction|Syntax: \033[0m")
        mylist = function_input.split("|")


        if function_input.lower().strip() == "deposit" :
            fataldict.update(tempdict)
            tempdict.clear()
            maxlen = max(max(len(x) for x in fataldict),9)
            with open('fatalfile.json', 'w') as handle:
                json.dump(fataldict, handle, sort_keys=True, indent = 2)
            with open("upshot.txt", "w") as listo:
                listo.write('{key: <{width}}    {value}'.format(key = "Function:",width = maxlen, value ="Syntax:\n"))
                sortdict = sorted(fataldict.items(), key = lambda x: x[0])
                for item in sortdict:
                    listo.write('{key: <{width}}    {value}\n'.format(key = item[0], width = maxlen, value = item[1]))
            print("Input(s) saved.")

            continue
            

        
        elif function_input.lower().strip() == "exit" :
            print("Entered functions erased")
            break

        
        

        elif len(mylist) != 2:
            print("\033[31mInvalid input. Please enter a valid function and syntax in the specified format.\033[0m")
            continue

        yek = mylist[0].strip()
        eulav = mylist[1].strip()
        tempdict[yek] = eulav

        print(f"\033[36mFunction inputted:\033[0m {yek}\033[36m  Syntax inputted:\033[0m {eulav}")

if __name__ == "__main__":
     main()




       
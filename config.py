# This File Contains Constants/etc
Locations = ("Delhi", "Jaipur")
Times =  ('Morning', 'Afternoon', 'Evening', 'Night')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Col:
    rst = "\033[0m" 
    bo = "\033[1m"  
    it = "\033[3m"  
    un = "\033[4m" 

    r = "\033[31m"
    g = "\033[32m" 
    y = "\033[33m" 
    b = "\033[34m" 
    p = "\033[35m"

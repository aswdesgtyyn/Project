import json
import os
from classes import Cab, RideRequest

Waiting_List = []


#--------------------------------------------------------------------------------------------------
#                                            Functions
#--------------------------------------------------------------------------------------------------

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def submit_request():
    pass

def find_matches():
    pass
def dispatch():
    pass


#--------------------------------------------------------------------------------------------------
while True:
    clear()
    print('|-------------------------------------------------------|')
    print('|                       Main Menu                       |')
    print('|-------------------------------------------------------|')
    print('|    1. Submit a Cab Request                            |')
    print('|    2. Find Matches                                    |')
    print('|    3. Dispatch a Cab                                  |')
    print('|    4. Exit Program                                    |')
    print('|-------------------------------------------------------|')
    
    try:
        o = int(input('|>'))
    except:
        print('!-!     Invalid Input    !-!')
        continue

    if o == 1:
        submit_request()
    elif o == 2:
        find_matches()
    elif o == 3:
        dispatch()
    elif o == 4:
        break
    else:
        print('!-!     Invalid Input    !-!')
        continue

clear()
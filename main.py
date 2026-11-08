import csv
import atexit
import os
from classes import Cab, RideRequest, Col

Waiting_List = []

#--------------------------------------------------------------------------------------------------
#                                            Functions
#--------------------------------------------------------------------------------------------------
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Save_All():
    clear()
    print(f'{Col.r}App Shutdown Detected!{Col.rst}')
    print(f'{Col.b}Saving App Data...{Col.rst}')

    # Impliment a Saving Function here




#--------------------------------------------------------------------------------------------------
atexit.register(Save_All)


Cab.Load_Data()
RideRequest.Load_Data()


while True:
    clear()
    print(f'|-------------------------------------------------------|')
    print(f'|{Col.bo}{Col.b}                       {Col.un}Main Menu{Col.rst}                       |')
    print(f'|-------------------------------------------------------|')
    print(f'|{Col.bo}    1. Submit a Cab Request                            {Col.rst}|')
    print(f'|{Col.bo}    2. Find Matches                                    {Col.rst}|')
    print(f'|{Col.bo}    3. Dispatch a Cab                                  {Col.rst}|')
    print(f'|{Col.bo}    4. Show All Cabs                                   {Col.rst}|')
    print(f'|{Col.bo}{Col.r}    5. Exit the Program                                {Col.rst}|')
    print(f'|-------------------------------------------------------|')
    o=0
    try:
        o = int(input('|>'))
    except:
        clear()
        print(f'{Col.bo}{Col.r}!-!   Invalid Input    !-!{Col.rst}')
        print('Press Enter to Continue...')
        input()
        continue

    if o == 1:
        pass
    elif o == 2:
        pass
    elif o == 3:
        pass
    elif o == 4:
        Cab.Show()
    elif o == 5:
        break
    else:
        clear()
        print(f'{Col.bo}{Col.r}!-!   Invalid Input    !-!{Col.rst}')
        print('Press Enter to Continue...')
        input()
        continue

clear()
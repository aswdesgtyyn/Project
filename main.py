import csv
import os
from classes import Cab, RideRequest

Waiting_List = []
Cabs = []

#--------------------------------------------------------------------------------------------------
#                                            Functions
#--------------------------------------------------------------------------------------------------

def Load_Cab_Data():
    l = []
    try:
        fin = open('cab_data.csv', newline='\n', mode='r')
        reader = csv.DictReader(fin, delimiter=',')

        for row in reader:
            obj = Cab(row['Driver Name'], row['Destination'], int(row['Max Seats']), row['Time'], False if row['Left'] == 'False' else True)
            l.append(obj)
    
        fin.close()
        return l
    except:
        print('Error in Reading cab_data.csv')
        return []


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#--------------------------------------------------------------------------------------------------

Cabs = Load_Cab_Data()

Condition = bool(Cabs) 


while Condition:
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
        pass
    elif o == 2:
        pass
    elif o == 3:
        pass
    elif o == 4:
        break
    else:
        print('!-!     Invalid Input    !-!')
        continue

clear()
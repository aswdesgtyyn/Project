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
    
    fin = open('cab_data.csv', newline='\n', mode='r')
    reader = csv.DictReader(fin, delimiter=',')

    for row in reader:
        obj = Cab(row['Driver Name'], row['Destination'], int(row['Max Seats']), row['Time'], False if row['Left'] == 'False' else True, [])
        l.append(obj)
    
    fin.close()
    return l
    

def Show_Cabs():
    print('|-------------------------------------------------------|')
    print('|                     List of Cabs                      |')
    print('|-------------------------------------------------------|')
    print('Driver Name\tDestination\tTime\tSeats\tAvailibilty')
    for a in Cabs:
        print(f"{a.driver_name}\t{a.destination}\t{a.time}\t{len(a.students)}/{a.max_seats}\t{"Available" if a.left else "Left"}")

    print('|-------------------------------------------------------|')
    print('| Press Enter to go back...                             |')
    print('|-------------------------------------------------------|')
    input('|>')

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
    print('|    4. Show All Cabs                                   |')
    print('|    5. Exit the Program                                |')
    print('|-------------------------------------------------------|')
    
    try:
        o = int(input('|>'))
    except:
        clear()
        print('!-!   Invalid Input    !-!')
        print('Press Enter to Continue...')

    if o == 1:
        pass
    elif o == 2:
        pass
    elif o == 3:
        pass
    elif o == 4:
        Show_Cabs()
    elif o == 5:
        break
    else:
        print('!-!   Invalid Input    !-!')
        continue

clear()
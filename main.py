import csv
import os
from classes import Cab, RideRequest, Col

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
    print('|------------------------------------------------------------------|')
    print(f'|                           {Col.bo}{Col.b}{Col.un}List of Cabs{Col.rst}                           |')
    print('|------------------------------------------------------------------|')
    print(f'|  {Col.bo}{'Driver Name':<20} {'Destination':<12} {'Time':<10} {'Seats':<5} {'Availibilty':<5}{Col.rst}  |')
    for a in Cabs:
        dn = a.driver_name

        des = a.destination
        des_c = Col.b if des[0] == 'D' else Col.y
        des = des_c + f"{des:<12}" + Col.rst

        tim = a.time
        stu = f'{len(a.students)}/{a.max_seats}'

        lef = f"{Col.g}Available  {Col.rst}" if a.left else f"{Col.r}Left       {Col.rst}"

        print(f"|  {dn:<20} {des} {tim:<10} {stu:<5} {lef:<5}  |")

    print('|------------------------------------------------------------------|')
    print('| Press Enter to go back...                                                  |')
    print('|------------------------------------------------------------------|')
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
        Show_Cabs()
    elif o == 5:
        break
    else:
        clear()
        print(f'{Col.bo}{Col.r}!-!   Invalid Input    !-!{Col.rst}')
        print('Press Enter to Continue...')
        input()
        continue

clear()
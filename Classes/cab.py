import json
import heapq
from Classes.config import Locations, Times, Col, clear, to_num
from Classes.ride_request import RideRequest



class Cab:
    Cabs = []   
    a = 0


    def __init__(self, driver_name :str, destination :str,  max_seats :int, time :str, left :bool, students :list[str]):

        if destination not in Locations:
            raise ValueError(f"{destination} is not in List of Permitted Locations")
        
        if max_seats > 4 and max_seats < 0:
            raise ValueError(f"Invalid Number of Seats, {max_seats}")
        
        if len(students) > max_seats:
            raise ValueError(f"Invalid Number of Students, {len(students)}")

        if time not in Times:
            raise ValueError(f"Invalid Time {time}")
        
        self.driver_name = driver_name
        self.destination = destination
        self.time = time
        self.max_seats = max_seats
        self.left = bool(left)
        self.students = list(students)

    @classmethod
    def Load_Data(cls):
        fin = open('data/cab_data.json', newline='\n', mode='r')
        data = json.load(fin)

        for row in data:
            obj = cls(row['Driver Name'], row['Destination'], int(row['Max Seats']), row['Time'], row['Left'], row['Seats'])
            (cls.Cabs).append(obj)
    
        fin.close()

    @classmethod
    def ToDict(cls):
        output = []
        for obj in cls.Cabs:
            d = {
                    "Driver Name": obj.driver_name,
                    "Destination": obj.destination,
                    "Time": obj.time,
                    "Max Seats": obj.max_seats,
                    "Left": obj.left,
                    "Seats": obj.students
                }
            output.append(d)
            
        return output


    @classmethod
    def Show(cls):
        print('|------------------------------------------------------------------|')
        print(f'|                           {Col.bo}{Col.b}{Col.un}List of Cabs{Col.rst}                           |')
        print('|------------------------------------------------------------------|')
        
        
        print(f'|  {Col.bo}{'Driver Name':<20} {'Destination':<12} {'Time':<10} {'Seats':<5} {'Availibilty':<5}{Col.rst}  |')
        
        
        for a in cls.Cabs:
            dn = a.driver_name

            des = a.destination
            des_c = Col.b if des[0] == 'D' else Col.y
            des = des_c + f"{des:<12}" + Col.rst

            tim = a.time
            stu = f'{len(a.students)}/{a.max_seats}'

            lef = f"{Col.g}Available  {Col.rst}" if a.left else f"{Col.r}Left       {Col.rst}"

            print(f"|  {dn:<20} {des} {tim:<10} {stu:<5} {lef:<5}  |")

    
        print('|------------------------------------------------------------------|')
        print('| Press Enter to go back...                                        |')
        print('|------------------------------------------------------------------|')
        input('|>')

    @classmethod
    def FindMatches(cls, ld):
        clear()
        print(f'|-----------------------------------------------------------------|')
        print(f'|                           {Col.bo}{Col.b}Find Matches{Col.rst}                          |')
        print(f'|-----------------------------------------------------------------|')


        for index, item in enumerate(cls.Cabs):

            if item.left:
                print(f"| {Col.b} Cab - {index:<3} Driver : {item.driver_name}")
                print(f"To : {Col.b if item.destination[0] == 'D' else Col.y}{item.destination}{Col.rst}")
                print("Student List")
                print(f"{'Name':<30} {'Year':<2} {'Desination':<10} {'Time':<5}")
                d, t = to_num(item.destination, item.time)

                m = ld[d][t]

                available = item.max_seats - len(item.students)
                preview = heapq.nsmallest(available, m)
                if not preview:
                    print('Seats Empty')
                else:
                    for x, w in enumerate(preview):
                        print(f'{w}')

                    if len(preview) < available:
                        print('Rest of Seats Empty')

        
        print(f'|-----------------------------------------------------------------|')
        print(f'{Col.bo} Press Enter to Continue... {Col.rst}')
        print(f'|-----------------------------------------------------------------|')
        input('|>')
        clear()
        return None

    @classmethod
    def Disp(cls):
        if not cls.a:
            clear()
            print(f"{Col.bo}{Col.r}Please Find Matches First!{Col.rst}")
            print('Press Enter to Continue...')
            input('|>')
            clear()

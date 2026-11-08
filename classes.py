import json

Locations = ("Delhi", "Jaipur")
Times =  ('Morning', 'Afternoon', 'Evening', 'Night')


class RideRequest:

    Requests = []

    def __init__(self, student_name :str, destination :str, time :str, year :int):
        
        if destination not in Locations:
            raise ValueError(f"{destination} is not in List of Permitted Locations")
            
        
        if year < 0 and year > 6:
            raise ValueError(f"Invalid Year, {year}")
            

        if time not in Times:
            raise ValueError(f"Invalid Time {time}")
            
        
        self.desination = destination
        self.year = year
        self.time = time
        self.student_name = student_name


    @classmethod
    def Load_Data(cls):
        fin = open('data/ride_data.json', newline='\n', mode='r')
        data = json.load(fin)

        for row in data:
            obj = cls(row['Student Name'], row['Destination'], row['Time'], row['Year'])
            (cls.Requests).append(obj)
        
        fin.close()



class Cab:
    Cabs = []


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
        print('| Press Enter to go back...                                                  |')
        print('|------------------------------------------------------------------|')
        input('|>')



# Colour Class
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

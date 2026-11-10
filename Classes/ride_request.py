import json
from Classes.config import Locations, Times, Col, clear


class RideRequest:
    Requests = []

    def __init__(self, student_name :str, destination :str, time :str, year :int, completed :bool):
        
        if destination not in Locations:
            raise ValueError(f"{destination} is not in List of Permitted Locations")
            
        
        if year < 0 and year > 6:
            raise ValueError(f"Invalid Year, {year}")
            

        if time not in Times:
            raise ValueError(f"Invalid Time {time}")
            
        
        self.destination = destination
        self.year = year
        self.time = time
        self.student_name = student_name
        self.completed = completed


    def __eq__(self, other):
        return (self.year == other.year) and (self.destination == other.destination)

    def __lt__(self, other):
        if self.destination == other.destination:
            return self.year > other.year
        else:
            return self.destination > other.destination

    def __gt__(self, other):
        if self.destination == other.destination:
            return self.year < other.year
        else:
            return self.destination < other.destination

    @classmethod
    def Load_Data(cls):
        fin = open('data/ride_data.json', newline='\n', mode='r')
        data = json.load(fin)

        for row in data:
            obj = cls(row['Student Name'], row['Destination'], row['Time'], row['Year'], row['Completed'])
            (cls.Requests).append(obj)
        
        fin.close()

    @classmethod
    def ToDict(cls):
        output = []
        for obj in cls.Requests:
            d =   {
                    "Student Name": obj.student_name,
                    "Destination": obj.destination,
                    "Time": obj.time,
                    "Completed": obj.completed,
                    "Year": obj.year
                }
            output.append(d)

        return output


    @classmethod
    def AddRequest(cls):
        while 1:
            clear()
            print(f'|-------------------------------------------------------|')
            print(f'|{Col.bo}{Col.g}                      {Col.un}Add Request{Col.rst}                      |')
            print(f'|-------------------------------------------------------|')
            print(f'| {Col.bo}Please Enter the Student Name{Col.rst}                         |')
            print(f'| Enter Blank to exit                                   |')
            print(f'|-------------------------------------------------------|')
            name = input('|>')

            if not name:
                break


            clear()
            print(f'|-------------------------------------------------------|')
            print(f'|{Col.bo}{Col.g}                      {Col.un}Add Request{Col.rst}                      |')
            print(f'|-------------------------------------------------------|')
            print(f'| Select the Destination.                               |')
            print(f'| 1. {Col.b}Delhi{Col.rst}                                              |')
            print(f'| 2. {Col.y}Jaipur{Col.rst}                                             |')
            print(f'|-------------------------------------------------------|')

            try:
                o = int(input('|>'))
            except:
                clear()
                print(f'{Col.r} Invalid Input please try again{Col.rst}')
                input('|>')
                clear()
                continue

            if o not in (1,2):
                clear()
                print(f'{Col.r} Invalid Input please try again{Col.rst}')
                input('|>')
                clear()
                continue

            dest = Locations[o-1]

            clear()
            print(f'|-------------------------------------------------------|')
            print(f'|{Col.bo}{Col.g}                      {Col.un}Add Request{Col.rst}                      |')
            print(f'|-------------------------------------------------------|')
            print(f'| Select the Time.                                      |')
            print(f'| 1. {Col.y}{Col.bo}Morning{Col.rst}                                            |')
            print(f'| 2. {Col.y}Afternoon{Col.rst}                                          |')
            print(f'| 3. {Col.b}Evening{Col.rst}                                            |')
            print(f'| 4. {Col.b}{Col.bo}Night{Col.rst}                                              |')
            print(f'|-------------------------------------------------------|')

            try:
                o = int(input('|>'))
            except:
                clear()
                print(f'{Col.r}Invalid Input please try again{Col.rst}')
                input('|>')
                clear()
                continue

            if o not in (1,2,3,4):
                clear()
                print(f'{Col.r}Invalid Input please try again{Col.rst}')
                input('|>')
                clear()
                continue

            tim = Times[o-1]

            clear()
            print(f'|-------------------------------------------------------|')
            print(f'|{Col.bo}{Col.g}                      {Col.un}Add Request{Col.rst}                      |')
            print(f'|-------------------------------------------------------|')
            print(f'| Please Enter Year of Study...                         |')
            print(f'|-------------------------------------------------------|')

            try:
                o = int(input('|>'))
            except:
                clear()
                print(f'{Col.r}Invalid Input please try again{Col.rst}')
                input('|>')
                clear()
                continue

            if o > 5 or o < 0:
                clear()
                print(f'{Col.r}Invalid Input please try again{Col.rst}')
                input('|>')
                clear()
                continue

            year = o

            obj = cls(name, dest, tim, year, False)
            cls.Requests.append(obj)

            clear()
            print(f'|-------------------------------------------------------|')
            print(f'|{Col.bo}{Col.g}                      {Col.un}Add Request{Col.rst}                      |')
            print(f'|-------------------------------------------------------|')
            print(f'|{Col.g}{Col.b} Request Successfully Added ! {Col.rst}.            |')
            print(f'| Press Enter to Continue...                            |')

            break




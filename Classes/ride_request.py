import json
from config import Locations, Times, Col, clear

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
        self.completed = False


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
                    "Year": obj.year
                }
            output.append(d)

        return output


    @classmethod
    def AddRequest(cls):
        clear()
        print(f'|-------------------------------------------------------|')
        print(f'|{Col.bo}{Col.g}                       {Col.un}Add Request{Col.rst}                       |')
        print(f'|-------------------------------------------------------|')
        input()
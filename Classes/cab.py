import json
import heapq
from Classes.config import Locations, Times, Col, clear, to_num
from Classes.ride_request import RideRequest



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
        try:
            fin = open('data/cab_data.json', newline='\n', mode='r')
        except:
            clear()
            print(f'{Col.r}{Col.bo}File is Missing/Corrupted !{Col.rst}')
            print(f'{Col.b}{Col.bo}Creating New Blank Files{Col.rst}')
            print('Press Enter to Continue')
            input('|>')

            fin = open('data/cab_data.json', newline='\n', mode='w')
            fin.close()
            return None
        data = json.load(fin)

        for row in data:
            obj = cls(row['Driver Name'], row['Destination'], int(row['Max Seats']), row['Time'], row['Left'], row['Seats'])
            (cls.Cabs).append(obj)
    
        fin.close()
        return None

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

            lef = f"{Col.g}Available  {Col.rst}" if not a.left else f"{Col.r}Left       {Col.rst}"

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

        temp_ld = [[queue[:] for queue in dest] for dest in ld]

        for index, item in enumerate(cls.Cabs):

            if item.left:
                print(f"|               {Col.bo} Cab - {index+1:<3} Driver : {item.driver_name} {Col.rst}")
                print(f"| {Col.bo}To : {Col.b if item.destination[0] == 'D' else Col.y}{item.destination}{Col.rst}{Col.bo}  ({item.time}) {Col.rst}")
                print(f'|                                                                 |')
                print(f"|                           {Col.g}{Col.bo}Student List{Col.rst}                          |")
                print(f"| {Col.bo}{'Name':<30} {'Year':<4} {' Desination':<10} {'Time':<5}{Col.rst}            ")
                d, t = to_num(item.destination, item.time)

                m = temp_ld[d][t]

                available = item.max_seats - len(item.students)
                for x in range(available):
                    if not m:
                        print(f'| Rest of Seats Empty                                             |')
                        break
                    w = heapq.heappop(m)
                    print(f'{w}')

                print(f'|                                                                 |')
                print(f'|-----------------------------------------------------------------|')
                print(f'|                                                                 |')

        
        print(f'|-----------------------------------------------------------------|')
        print(f'| {Col.bo}Press Enter to Continue...{Col.rst}                                      |')                                  
        print(f'|-----------------------------------------------------------------|')
        input('|>')
        clear()
        return None

    @classmethod
    def Disp(cls):
        clear()
        print(f'|---------------------------------------------------------------------------|')
        print(f'|                                {Col.un}{Col.bo}{Col.b}Dispatch a Cab{Col.rst}                             |')
        print(f'|---------------------------------------------------------------------------|')
        
        try:
            print(f'| Select Destination.                                                       |')
            print(f'| 1. Delhi                                                                  |')
            print(f'| 2. Jaipur                                                                 |')
            print(f'|---------------------------------------------------------------------------|')
            dest = Locations[int(input('|> ')) - 1]

            clear()

            print(f'|---------------------------------------------------------------------------|')
            print(f'|                                {Col.un}{Col.bo}{Col.b}Dispatch a Cab{Col.rst}                             |')
            print(f'|---------------------------------------------------------------------------|')
            print(f'| Select Destination.                                                       |')
            print(f'| 1. Morning                                                                |')
            print(f'| 2. Afternoon                                                              |')
            print(f'| 3. Evening                                                                |')
            print(f'| 4. Night                                                                  |')
            print(f'|---------------------------------------------------------------------------|')
            tim = Times[int(input('|> ')) - 1]
        except:
            print(f"{Col.r}{Col.bo}Invalid input.{Col.rst}")
            input('|> Press Enter...')
            return

        dest_id, tim_id = to_num(dest, tim)
        m = RideRequest.Heaps[dest_id][tim_id]

        target_cab = next((cab for cab in cls.Cabs if not cab.left and cab.destination == dest and cab.time == tim), None)
        
        if not target_cab:
            clear()
            print(f"{Col.r}No open cabs available for {dest} at {tim}.{Col.rst}")
            input('|>')
            return
            
        if not m:
            clear()
            print(f"{Col.r}No students waiting for this trip.{Col.rst}")
            input('|>')
            return

        available = target_cab.max_seats - len(target_cab.students)
        assigned = 0
        
        while m and assigned < available:
            try:
                student_req = heapq.heappop(m)
            except:
                print(f'{Col.bo}{Col.r}Not Enough Students to Fill Cab!{Col.r}')
                print('Enter 0 to Go Back, Enter 1 to still Dispatch')
                o = input('|>')

                if o == '0':
                    return None
                elif o == '1':
                    break
                else:
                    print('Invalid Option : Click Enter to Go Back')
                    input('|>')
                    return None
                
            target_cab.students.append(student_req.student_name)
            student_req.completed = True
            assigned += 1
            
        target_cab.left = True
        
        clear()
        print(f"{Col.g}Successfully dispatched {target_cab.driver_name}'s cab with {assigned} students!{Col.rst}")
        input('|>')

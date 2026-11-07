Locations = ("Delhi", "Jaipur")
Times =  ('Morning', 'Afternoon', 'Evening', 'Night')


class RideRequest:
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




class Cab:
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

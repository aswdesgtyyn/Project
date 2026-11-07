Locations = ("Delhi", "Jaipur")
Years = (1, 2, 3, 4, 5)
Times =  ('Morning', 'Afternoon', 'Evening', 'Night')


class RideRequest:
    def __innit__(self, student_name :str, destination :str, time :str, year :int):
        
        if destination not in Locations:
            print(f"{destination} is not in List of Permited Locations")
            return 0
        
        if year not in Years:
            print(f"year {year} does not exist")
            return 0

        if time not in Times:
            print(f"Invalid Time {time}")
            return 0
        
        self.desination = destination
        self.year = year
        self.time = time
        self.student_name = student_name

        return 1


class Cab:
    def __innit__(self, driver_name :str, destination :str,  max_seats :int, time :str, left :bool, students :list[str]):

        if destination not in Locations:
            print(f"{destination} is not in List of Permited Locations")
            return 0
        
        if max_seats < 5 and max_seats > 0:
            print(f'Invalid Number of Seats, {max_seats}')
            return 0
        
        if len(students) > 4:
            print(f'Invalid Number of Students, {len(students)}')
            return 0

        if time not in Times:
            print(f"Invalid Time {time}")
            return 0

        self.driver_name = driver_name
        self.destination = destination
        self.time = time
        self.left = bool(left)
        self.students = list(students)


        return 1

import json
import sys
import os


#--------------------------------------------------------------------------------------------------
#                                           Parameters
#--------------------------------------------------------------------------------------------------
Locations = ("Delhi", "Jaipur")
Years = ('1', '2', '3', '4', '5')
Times =  ('Morning', 'Afternoon', 'Evening', 'Night')

#--------------------------------------------------------------------------------------------------
#                                            Classes
#--------------------------------------------------------------------------------------------------
class RideRequest:
    def __innit__(self, student_name, destination, time, year):
        
        if destination not in Locations:
            print(f"{desination} is not in List of Permited Locations")
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
    def __innit__(self, driver_name, destination,  num_seats, students):

        if destination not in Locations:
            print(f"{desination} is not in List of Permited Locations")
            return 0
        
        if num_seats not in Num_Seats:
            print(f'Invalid Number of Seats, {num_seats}')
            return 0
        
        if len(students) > 4:
            print(f'Invalid Number of Students, {len(students)}')

        self.driver_name = driver_name
        self.destination = destination
        self.students = list(students)

        return 1



    


#--------------------------------------------------------------------------------------------------
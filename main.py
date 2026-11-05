import json
import sys
import os


#--------------------------------------------------------------------------------------------------
#                                           Parameters
#--------------------------------------------------------------------------------------------------
Locations = ("Delhi", "Jaipur")
years = ('1', '2', '3', '4', '5')


#--------------------------------------------------------------------------------------------------
#                                            Classes
#--------------------------------------------------------------------------------------------------
class RideRequest:
    def __innit__(self, student_name, destination, time, year):
        if destination in Locations:
            self.desination = destination
        else:
            print(f"{desination} is not in List of Permited Locations")
            return 0
        
        if year in years:
            self.year = year
        else:
            print(f"year {year} does not exist")
            return 0

        self.student_name = student_name
        self.time = time

        return 1



#--------------------------------------------------------------------------------------------------
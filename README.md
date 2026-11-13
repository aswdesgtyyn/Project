# Cab Project ig

> **Note**
> Please Run this Project in a Terminal which supoorts coloured Text!
>

## Project Structure
├── Classes
│   ├── __init__.py
│   ├── cab.py
│   ├── config.py
│   └── ride_request.py
├── README.md
├── data
│   ├── cab_data.json
│   └── ride_data.json
├── main.py
└── reset_data.py


## main.py
The Main Python File, Contains the Main Menu and Save All Functions. 


## reset_data.py
Resets the Data of the cab_data.json and the ride_data.json file.

## Classes/cab.py
Contains the Cab Class and the Related Class Functions.
Mainly Contains the following Functions,
- Show        -> Showing All the Cabs
- FindMatches -> For Finding Matches of Cabs
- Disp        -> Dispaching the Cabs

## Classes/riderequest.py
Contains the Ride Request Class, Comparitively Smaller in Comparision to the Cab Class
Mainly Contains the following Function,
- AddRequest -> For Adding a Request

## Classes/config.py
Contains Mainly the Support Functions for main.py, cab.py and ride_request.py
Mainly contains the clear() function for clearing the screen and the Color Class for Handling the Text Colours

---
### Note
- To Generate the Dummy Data i.e. cab_data.json and ride_data.json AI has been used with permission.
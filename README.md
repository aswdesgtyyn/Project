# Cab Project ig

> **Note**
> Please Run this Project in a Terminal which supoorts coloured Text!
>

## Project Structure
``` tree
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
```

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
## Brownie Point Things Done
 - App Saves the Current State upon closing
 - Even if it Crashes or Ctrl - C is hit App will still save before shutting down
    - Note it does not save after each change but will save at each exit
 - After Saving and After Loading the Order of the Requests is Maintained
 - Even if Data Files do not exist App Does not crash and creates new blank files
 - JSON was used as the Format of the Data rather than CSV, XML or pickle (Binary Files) because
    - JSON has analogues for all major python data types and can be loaded and dumped easily through singular Functions
 - If two students are in the same year the one who Requested first will get priority.
 - If a Cab is Half Empty / Has Vacant Seats but no Student to for it to be occupied by
    - The user is informed and given an option to either still dispatch or go back to main menu

---
### Note
- To Generate the Dummy Data i.e. cab_data.json and ride_data.json AI has been used with permission.

fin = open('data/cab_data.json', 'w')

cab = """[
  {
    "Driver Name": "Paresh Shan",
    "Destination": "Jaipur",
    "Time": "Night",
    "Max Seats": 4,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Dilip Kumar",
    "Destination": "Delhi",
    "Time": "Night",
    "Max Seats": 1,
    "Left": false,
    "Seats": []
  },
  {
    "Driver Name": "Ravioli Sharma",
    "Destination": "Jaipur",
    "Time": "Night",
    "Max Seats": 1,
    "Left": false,
    "Seats": []
  },
  {
    "Driver Name": "Badal Speed",
    "Destination": "Delhi",
    "Time": "Afternoon",
    "Max Seats": 4,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Akash Vani",
    "Destination": "Jaipur",
    "Time": "Evening",
    "Max Seats": 4,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Gaddi Prasad",
    "Destination": "Jaipur",
    "Time": "Night",
    "Max Seats": 1,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Break Fail Kapoor",
    "Destination": "Jaipur",
    "Time": "Night",
    "Max Seats": 4,
    "Left": false,
    "Seats": []
  },
  {
    "Driver Name": "Speedy Singh",
    "Destination": "Jaipur",
    "Time": "Morning",
    "Max Seats": 2,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Sultan Of Swag",
    "Destination": "Delhi",
    "Time": "Night",
    "Max Seats": 3,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Chal Bhaag Verma",
    "Destination": "Delhi",
    "Time": "Afternoon",
    "Max Seats": 2,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Chai Pilo Gupta",
    "Destination": "Jaipur",
    "Time": "Afternoon",
    "Max Seats": 2,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Horn Ok Please",
    "Destination": "Jaipur",
    "Time": "Afternoon",
    "Max Seats": 3,
    "Left": false,
    "Seats": []
  },
  {
    "Driver Name": "U-Turn Yadav",
    "Destination": "Delhi",
    "Time": "Evening",
    "Max Seats": 3,
    "Left": false,
    "Seats": []
  },
  {
    "Driver Name": "Drift Raja",
    "Destination": "Jaipur",
    "Time": "Afternoon",
    "Max Seats": 3,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Jaldi Karo Joshi",
    "Destination": "Delhi",
    "Time": "Night",
    "Max Seats": 4,
    "Left": false,
    "Seats": []
  },
  {
    "Driver Name": "No Signal Sen",
    "Destination": "Jaipur",
    "Time": "Night",
    "Max Seats": 2,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Over Take Oberoi",
    "Destination": "Jaipur",
    "Time": "Evening",
    "Max Seats": 1,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Puncture Patel",
    "Destination": "Jaipur",
    "Time": "Morning",
    "Max Seats": 3,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Chalan Chandran",
    "Destination": "Jaipur",
    "Time": "Night",
    "Max Seats": 3,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Full Speed Shukla",
    "Destination": "Delhi",
    "Time": "Night",
    "Max Seats": 2,
    "Left": false,
    "Seats": []
  },
  {
    "Driver Name": "Traffic Jam Tandon",
    "Destination": "Delhi",
    "Time": "Morning",
    "Max Seats": 2,
    "Left": false,
    "Seats": []
  },
  {
    "Driver Name": "Meter Down Menon",
    "Destination": "Jaipur",
    "Time": "Night",
    "Max Seats": 2,
    "Left": true,
    "Seats": []
  },
  {
    "Driver Name": "Honk Lal",
    "Destination": "Delhi",
    "Time": "Morning",
    "Max Seats": 1,
    "Left": false,
    "Seats": []
  }
]"""

fin.write(cab)
fin.close()

fin = open('data/ride_data.json', 'w')

ride = """[
    {
        "Student Name": "Maggi Sharma",
        "Destination": "Delhi",
        "Time": "Night",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Backbench Patel",
        "Destination": "Delhi",
        "Time": "Morning",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Proxy Verma",
        "Destination": "Delhi",
        "Time": "Night",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Chai Sutta Singh",
        "Destination": "Delhi",
        "Time": "Night",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Sleepless Sen",
        "Destination": "Delhi",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "Assignment Roy",
        "Destination": "Delhi",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 2
    },
    {
        "Student Name": "Night Owl Nambiar",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Mass Bunk Mukherjee",
        "Destination": "Jaipur",
        "Time": "Morning",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Grace Marks Gupta",
        "Destination": "Jaipur",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Canteen Kumar",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Syllabus Outside Sharma",
        "Destination": "Jaipur",
        "Time": "Night",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Late Latif Lal",
        "Destination": "Delhi",
        "Time": "Night",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Kallu Coffee",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Viva Victim Vyas",
        "Destination": "Jaipur",
        "Time": "Evening",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Attendance Low Joshi",
        "Destination": "Delhi",
        "Time": "Night",
        "Completed" : false,
        "Year": 2
    },
    {
        "Student Name": "Detained Deshmukh",
        "Destination": "Jaipur",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Copy Paste Chawla",
        "Destination": "Jaipur",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "Internal Marks Iyer",
        "Destination": "Delhi",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Lab Record Reddi",
        "Destination": "Delhi",
        "Time": "Night",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Firr Se Fail Kulkarni",
        "Destination": "Jaipur",
        "Time": "Night",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Last Minute Mahajan",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "KT Kumar",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "Canteen Dues Das",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Prac Exam Prasad",
        "Destination": "Jaipur",
        "Time": "Evening",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Viva Vacant Varma",
        "Destination": "Jaipur",
        "Time": "Evening",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Backlog Bhandari",
        "Destination": "Jaipur",
        "Time": "Night",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "Maggi Masala Mehta",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "Noc Clearance Nair",
        "Destination": "Jaipur",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Group Project Goyal",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Syllabus Scared Shah",
        "Destination": "Delhi",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Chai Break Chhabra",
        "Destination": "Jaipur",
        "Time": "Evening",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Late Submission Saxena",
        "Destination": "Jaipur",
        "Time": "Evening",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Proxy King Kapoor",
        "Destination": "Jaipur",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Re-evaluation Rao",
        "Destination": "Delhi",
        "Time": "Morning",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Hostel Gate Hedgewar",
        "Destination": "Jaipur",
        "Time": "Night",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Night Study Naidu",
        "Destination": "Jaipur",
        "Time": "Morning",
        "Completed" : false,
        "Year": 2
    },
    {
        "Student Name": "Attendance Shortage Swamy",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Copying Expert Edmonds",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "Zero Internal Sen",
        "Destination": "Jaipur",
        "Time": "Morning",
        "Completed" : false,
        "Year": 3
    },
    {
        "Student Name": "Mass Bunk Mishra",
        "Destination": "Jaipur",
        "Time": "Morning",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "Doubt Clearing Dutta",
        "Destination": "Jaipur",
        "Time": "Morning",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Backbencher Bhatnagar",
        "Destination": "Jaipur",
        "Time": "Evening",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Canteen Credit Chaudhry",
        "Destination": "Delhi",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Fail Phobia Pandey",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "Extra Sheet Grover",
        "Destination": "Jaipur",
        "Time": "Morning",
        "Completed" : false,
        "Year": 2
    },
    {
        "Student Name": "Lab Coat Lamba",
        "Destination": "Jaipur",
        "Time": "Evening",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Unit Test Trivedi",
        "Destination": "Jaipur",
        "Time": "Morning",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Midsem Panic Puri",
        "Destination": "Delhi",
        "Time": "Night",
        "Completed" : false,
        "Year": 4
    },
    {
        "Student Name": "Grace Mark Ghosal",
        "Destination": "Delhi",
        "Time": "Morning",
        "Completed" : false,
        "Year": 5
    },
    {
        "Student Name": "Syllabus Skip Sethi",
        "Destination": "Jaipur",
        "Time": "Afternoon",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Attendance Fraud Farooqui",
        "Destination": "Delhi",
        "Time": "Evening",
        "Completed" : false,
        "Year": 1
    },
    {
        "Student Name": "Degree Delayed Deshmukh",
        "Destination": "Jaipur",
        "Time": "Evening",
        "Completed" : false,
        "Year": 1
    }
]"""

fin.write(ride)

fin.close()
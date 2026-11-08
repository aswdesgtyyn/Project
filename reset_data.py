fin = open('data/cab_data.csv', 'w')

cab = """Driver Name,Destination,Time,Max Seats,Left
Paresh Shan,Jaipur,Night,4,True
Dilip Kumar,Delhi,Night,1,False
Ravioli Sharma,Jaipur,Night,1,False
Badal Speed,Delhi,Afternoon,4,True
Akash Vani,Jaipur,Evening,4,True
Gaddi Prasad,Jaipur,Night,1,True
Break Fail Kapoor,Jaipur,Night,4,False
Speedy Singh,Jaipur,Morning,2,True
Sultan Of Swag,Delhi,Night,3,True
Chal Bhaag Verma,Delhi,Afternoon,2,True
Chai Pilo Gupta,Jaipur,Afternoon,2,True
Horn Ok Please,Jaipur,Afternoon,3,False
U-Turn Yadav,Delhi,Evening,3,False
Drift Raja,Jaipur,Afternoon,3,True
Jaldi Karo Joshi,Delhi,Night,4,False
No Signal Sen,Jaipur,Night,2,True
Over Take Oberoi,Jaipur,Evening,1,True
Puncture Patel,Jaipur,Morning,3,True
Chalan Chandran,Jaipur,Night,3,True
Full Speed Shukla,Delhi,Night,2,False
Traffic Jam Tandon,Delhi,Morning,2,False
Meter Down Menon,Jaipur,Night,2,True
Honk Lal,Delhi,Morning,1,False
"""

fin.write(cab)
fin.close()

fin = open('data/ride_data.csv', 'w')

ride = """Student Name,Destination,Time,Year
Maggi Sharma,Delhi,Night,1
Backbench Patel,Delhi,Morning,3
Proxy Verma,Delhi,Night,1
Chai Sutta Singh,Delhi,Night,1
Sleepless Sen,Delhi,Afternoon,5
Assignment Roy,Delhi,Afternoon,2
Night Owl Nambiar,Delhi,Evening,4
Mass Bunk Mukherjee,Jaipur,Morning,3
Grace Marks Gupta,Jaipur,Afternoon,1
Canteen Kumar,Delhi,Evening,1
Syllabus Outside Sharma,Jaipur,Night,4
Late Latif Lal,Delhi,Night,1
Kallu Coffee,Delhi,Evening,1
Viva Victim Vyas,Jaipur,Evening,3
Attendance Low Joshi,Delhi,Night,2
Detained Deshmukh,Jaipur,Afternoon,4
Copy Paste Chawla,Jaipur,Afternoon,5
Internal Marks Iyer,Delhi,Afternoon,3
Lab Record Reddi,Delhi,Night,1
Firr Se Fail Kulkarni,Jaipur,Night,1
Last Minute Mahajan,Delhi,Evening,5
KT Kumar,Delhi,Evening,5
Canteen Dues Das,Delhi,Evening,3
Prac Exam Prasad,Jaipur,Evening,4
Viva Vacant Varma,Jaipur,Evening,1
Backlog Bhandari,Jaipur,Night,5
Maggi Masala Mehta,Delhi,Evening,5
Noc Clearance Nair,Jaipur,Afternoon,1
Group Project Goyal,Delhi,Evening,3
Syllabus Scared Shah,Delhi,Afternoon,1
Chai Break Chhabra,Jaipur,Evening,1
Late Submission Saxena,Jaipur,Evening,3
Proxy King Kapoor,Jaipur,Afternoon,3
Re-evaluation Rao,Delhi,Morning,4
Hostel Gate Hedgewar,Jaipur,Night,3
Night Study Naidu,Jaipur,Morning,2
Attendance Shortage Swamy,Delhi,Evening,4
Copying Expert Edmonds,Delhi,Evening,5
Zero Internal Sen,Jaipur,Morning,3
Mass Bunk Mishra,Jaipur,Morning,5
Doubt Clearing Dutta,Jaipur,Morning,4
Backbencher Bhatnagar,Jaipur,Evening,4
Canteen Credit Chaudhry,Delhi,Afternoon,4
Fail Phobia Pandey,Delhi,Evening,5
Extra Sheet Grover,Jaipur,Morning,2
Lab Coat Lamba,Jaipur,Evening,1
Unit Test Trivedi,Jaipur,Morning,4
Midsem Panic Puri,Delhi,Night,4
Grace Mark Ghosal,Delhi,Morning,5
Syllabus Skip Sethi,Jaipur,Afternoon,1
Attendance Fraud Farooqui,Delhi,Evening,1
Degree Delayed Deshmukh,Jaipur,Evening,1"""

fin.write(ride)

fin.close()
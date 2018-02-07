import os
import csv

# just a way to let us open the data in a loop, since our test csvs are
employee_data = ['1', '2']

# loop so we can go over multiple files!
for employeedata in employee_data:
    
   file = os.path.join('raw_data', 'employee_data'+ str(employeedata) + ".csv")
#states dictionary
   states = { 
       'Alabama': 'AL',
       'Alaska': 'AK',
       'Arizona': 'AZ',
       'Arkansas': 'AR',
       'California': 'CA',
       'Colorado': 'CO',
       'Connecticut': 'CT',
       'Delaware': 'DE',
       'Florida': 'FL',
       'Georgia': 'GA',
       'Hawaii': 'HI',
       'Idaho': 'ID',
       'Illinois': 'IL',
       'Indiana': 'IN',
       'Iowa': 'IA',
       'Kansas': 'KS',
       'Kentucky': 'KY',
       'Louisiana': 'LA',
       'Maine': 'ME',
       'Maryland': 'MD',
       'Massachusetts': 'MA',
       'Michigan': 'MI',
       'Minnesota': 'MN',
       'Mississippi': 'MS',
       'Missouri': 'MO',
       'Montana': 'MT',
       'Nebraska': 'NE',
       'Nevada': 'NV',
       'New Hampshire': 'NH',
       'New Jersey': 'NJ',
       'New Mexico': 'NM',
       'New York': 'NY',
       'North Carolina': 'NC',
       'North Dakota': 'ND',
       'Ohio': 'OH',
       'Oklahoma': 'OK',
       'Oregon': 'OR',
       'Pennsylvania': 'PA',
       'Rhode Island': 'RI',
       'South Carolina': 'SC',
       'South Dakota': 'SD',
       'Tennessee': 'TN',
       'Texas': 'TX',
       'Utah': 'UT',
       'Vermont': 'VT',
       'Virginia': 'VA',
       'Washington': 'WA',
       'West Virginia': 'WV',
       'Wisconsin': 'WI',
       'Wyoming': 'WY',}

   #create lists based on output data
   emp_id = []
   fname = []
   lname = []
   bday = []
   ssn = []
   state = []

   #read csv, append data
   with open(file, 'r') as csvfile:

       reader = csv.DictReader(csvfile)

       for row in reader:

           emp_id.append(row['Emp ID'])
           fname.append(row['Name'].split(" ")[0])
           lname.append(row['Name'].split(" ")[1])
           bday.append(row['DOB'])
           ssn.append('***-**-' + row['SSN'].split('-')[2])
           state.append(states[row['State']])

   #zip
   emplyeedata = zip(emp_id, fname, lname, bday, ssn, state)

   #output
   output = os.path.join('output', 'new_employee_data' + str(employeedata) + '.csv')

   with open(output, 'w') as csvwrite:

       newfile = csv.writer(csvwrite, delimiter = ",")
       newfile.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
       newfile.writerows(emplyeedata)
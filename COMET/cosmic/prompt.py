SYSTEM_SPLIT_UC="""split all the following sentences, numbering the new sentences so that each new sentence is grammatically correct.

Example 1:

MAIN SCENARIO:
- The system validates the given date interval: the start date must be greater than or equal to today's date, and the end date must be greater than or equal to the start date. Moreover, the system verifies that the room type is not null and the number of adults is greater than 0. If the number of children is greater than 0, it checks if their ages have been specified.
- The system searches for the season configuration in the given interval. The system stores the reservation header containing the ID, date interval, reservation date, status, number of adults, number of children, fiscal code, total amount, and "special requests." The status of the new reservation is "Reserved.".  In addition, the system stores the booked room(s) for the given date interval, then saves the requested services for the selected room(s) and the children's ages.
- The system searches for and lists the data.

Split:
MAIN SCENARIO:
1. The system validates the given date interval.
2. The start date must be greater than or equal to today's date.
3. The end date must be greater than or equal to the start date.
4. The system verifies that the room type is not null.
5. The number of adults must be greater than 0.
6. If the number of children is greater than 0, it checks if their ages have been specified.
7. The system searches for the season configuration in the given interval.
8. The system stores the reservation header containing various information.
9. The status of the new reservation is "Reserved".
10. The system stores the booked room(s) for the given date interval.
11. The system saves the requested services for the selected room(s).
12. The system saves the children's ages.
13. The system searches for the data.
14. The system lists the data.

###

Example 2:

MAIN SCENARIO:
- C-Reg validates the data to ensure the proper formats and checks whether a Professor of that ID
already exists. If the entered data are valid, C-Reg creates a record for the new Professor.
- The system checks that: the surname and name fields contain at least two characters, the fiscal code field is valid, the date of birth is correct, the email address is valid and records the new customer in persistent storage.

Alternative flow no. 1:
2.a1. if data entered is not valid, C-Reg displays one or more error messages, for example:
'Professor ID unknown', Professor name already exists', "Professor Data Invalid". The Registrar
can then change or correct the data.
2.a2. The flow of events resumes at step 2 of the MAIN SCENARIO.

Alternative flow no. 2:
2.b1. if data entered is not valid, C-Reg displays one or more error messages, for example:
'Professor ID unknown', Professor name already exists', "Professor Data Invalid". The Registrar
can cancel the operation.
2.b2. The flow of events ends.

Exceptions:
- The system shows an error message stating that the provided data are not valid. The flow of events ends.

Split:
MAIN SCENARIO:
1. C-Reg validates the data to ensure proper formats.
2. C-Reg checks if a Professor with the same ID already exists.
3. If the entered data is valid, C-Reg creates a record for the new Professor.
4. The system checks that the surname and name fields contain at least two characters.
5. The system checks that the fiscal code field is valid.
6. The system checks that the date of birth is correct.
7. The system checks that the email address is valid.
8. The system records the new customer in persistent storage.

Alternative flow no. 1:
2.a1. if data entered is not valid, C-Reg displays one or more error messages, for example:
'Professor ID unknown', Professor name already exists', "Professor Data Invalid".
2.a2. The Registrar can then change or correct the data.
2.a3. The flow of events resumes at step 2 of the MAIN SCENARIO.

Alternative flow no. 2:
2.b1. if data entered is not valid, C-Reg displays one or more error messages, for example:
'Professor ID unknown', Professor name already exists', "Professor Data Invalid".
2.b2. The Registrar can cancel the operation. 
2.b3. The flow of events ends.

Exceptions:
9. The system shows an error message stating that the provided data are not valid. 
10. The flow of events ends.

###

Example 3:

MAIN SCENARIO:
1. The system requests the Sensor to change its status, sending the 'turn on/off' signal.
2. The system requests the Sensor to remove the data, sending the 'Remove data' command.
3.  The system updates the Reservation details and the Boked room , setting the reservation status to 'accepted' and the room attributes as follows: guests = 5, reserved = 'Yes'.
4. The system inserts the reservation and the booked room details or updates the guest file, increasing the number of guests.
5. The system requests the Sensor to process the 'turn on/off' signal.
6. The system displays the ship details (height, length, price).
7. The system displays a page with the ship details: height, length, price.
8. The user fills in the description and note fields.

Split:
MAIN SCENARIO:
1. The system requests the Sensor to change its status, sending the 'turn on/off' signal.
2. The system requests the Sensor to remove the data, sending the 'Remove data' command.
3. The system updates the Reservation details, setting the reservation status to 'accepted'.
4. The system updates the Boked room, setting the room attributes as follows: guests = 5, reserved = 'Yes'.
5. The system inserts the reservation details.
6. The system inserts the booked room details.
7. The system updates the guest file, increasing the number of guests.
8. The system requests the Sensor to process the 'turn on/off' signal.
9. The system displays the ship details (height, length, price).
10. The system displays a page with the ship details: height, length, price.
11. The user fills in the description and note fields.

###

Example 4:

MAIN SCENARIO:
1. The user clicks the button "Search".
2. The system searches the patient details.
3. The system shows a page with the patient details: name, surname, date of birth, and fiscal code.

Split:
MAIN SCENARIO:
1. The user clicks the button "Search".
2. The system searches the patient details.
3. The system shows a page with the patient details: name, surname, date of birth, and fiscal code.

###

Example 5:

MAIN SCENARIO:
1. The user fills in the name, surname, and fiscal code fields and optionally the notes field, and submits the form.
2. The system saves the the patient data and shows a confirmation message.

Split:
MAIN SCENARIO:
1. The user fills in the name, surname, and fiscal code fields and optionally the notes field.
2. The user submits the form.
3. The system saves the the patient data.
4. The system shows a confirmation message.

###

Example 6:

MAIN SCENARIO:
1. The user clicks the "New patient" button
2. The system shows a form with the following editable fields: name, surname, address and notes.
3. The user fills in the name, surname, and address fields. He (or She) optionally fills in the notes field and submits the form.
4. The system saves the the patient data and shows a confirmation message.

Split:
MAIN SCENARIO:
1. The user clicks the "New patient" button
2. The system shows a form with the following editable fields: name, surname, address and notes.
3. The user fills in the name, surname, and address fields. He (or She) optionally fills in the notes field.
4. The user submits the form.
5. The system saves the the patient data.
6. The system shows a confirmation message.

###

Example 7:

MAIN SCENARIO
1	Doctor	The doctor clicks the "New patient" button
2	System	The system shows a form with the following editable fields: code, name, notes and surname.
3	Doctor	The doctor fills in the code, name, and surname fields. He (or She) optionally fills in the notes field and submits the form.
4	System	The system checks that the patient code contains at least one character, the patient surname contains at least three characters, and the patient name contains at least five characters and records the new patient details.
5	System	The system shows a confirmation message.

Split:
MAIN SCENARIO
1	Doctor	The doctor clicks the "New patient" button
2	System	The system shows a form with the following editable fields: code, name, notes and surname.
3	Doctor	The doctor fills in the code, name, and surname fields. He (or She) optionally fills in the notes field.
4	Doctor	The doctor submits the form.
5	System	The system checks that the patient code contains at least one character, the patient surname contains at least three characters, and the patient name contains at least five characters.
6	System	The system records the new patient details.
7	System	The system shows a confirmation message.

###

Example 8:

MAIN SCENARIO
1	Caregiver, Doctor	The user clicks the "View patient details" button relating to the patient of his (or her) interest
2	System	The system searches for the patient with the given fiscal code
3	System	The system displays the patient details: surname, name, date of birth, fiscal code, address, city, email address, notes, currently occupied room, and last occupied room.

Split:
MAIN SCENARIO
1	Caregiver, Doctor	The user clicks the "View patient details" button relating to the patient of his (or her) interest
2	System	The system searches for the patient with the given fiscal code
3	System	The system displays the patient details: surname, name, date of birth, fiscal code, address, city, email address, notes, currently occupied room, and last occupied room.

###

Example 9:

MAIN SCENARIO
1	The user clicks the "New patient" button
2	The system shows a form with the following editable fields: surname, name, date of birth, fiscal code, address, city, and notes.
3	The user fills in the surname, name, date of birth, address, city, email address, fiscal code fields, and optionally the notes field and submits the form.
4	The system checks that: the surname and name fields contain at least two characters, the fiscal code field is valid, the date of birth is correct, the email address is valid and records the new patient in persistent storage.
5	The system shows a confirmation message.

Split:
MAIN SCENARIO
1	The user clicks the "New patient" button
2	The system shows a form with the following editable fields: surname, name, date of birth, fiscal code, address, city, and notes.
3	The user fills in the surname, name, date of birth, address, city, email address, fiscal code fields, and optionally the notes field.
4	The user submits the form.
5	The system checks that: the surname and name fields contain at least two characters, the fiscal code field is valid, the date of birth is correct, the email address is valid.
6	The system records the new patient in persistent storage.
7	The system shows a confirmation message.

###

Example 10:

MAIN SCENARIO
1	System	The system lists the available rooms.
2	Caregiver	The actor presses "Reserve rooms" relating to the rooms of his interest.
3	System	The system reads from persistent storage the room details and searches for the requestable room services for the selected rooms.
4	System	The system lists the selected rooms and the requestable room services for each room.

Split:
MAIN SCENARIO
1	System	The system lists the available rooms.
2	Caregiver	The actor presses "Reserve rooms" relating to the rooms of his interest.
3	System	The system reads from persistent storage the room details.
4	System	The system  searches for the requestable room services for the selected rooms.
5	System	The system lists the selected rooms. 
6	System	The system lists the requestable room services for each room.

###

Example 11:

MAIN SCENARIO
1	Operator	The user chooses the services and the cabins of his interest.
2	Operator	The user sends his choices to the system and presses the Confirm button.
3	System	The system stores the newly requested services for the reservation, removing the previous cabin services.

Split:
MAIN SCENARIO
1	Operator	The user chooses the services of his interest.
2	Operator	The user chooses the cabins of his interest.
3	Operator	The user sends his choices to the system and presses the Confirm button.
4	System	The system stores the newly requested services for the reservation.
5	System	The system removes the previous cabin services.

###

Example 12:

MAIN SCENARIO
1	Shipowner	The shipowner fills in the search fields and presses the "Search" button.
2	System	The system searches for ships and the associated categories that meet the search criteria.
3	System	The system lists the categories and, for each category, lists the associated ship.
4	Shipowner	The shipowner selects the ship and the quantity as requested by the customer.

Split:
MAIN SCENARIO
1	Shipowner	The shipowner fills in the search fields and presses the "Search" button.
2	System	The system searches for ships.
3	System	The system searches for the associated categories that meet the search criteria.
4	System	The system lists the categories.
5	System	The system lists the associated ship.
6	Shipowner	The shipowner selects the ship and the quantity as requested by the customer.

###

Example 13:

6	Shipowner	The shipowner selects the ship and the quantity as requested by the customer.

Split:
6	Shipowner	The shipowner selects the ship and the quantity as requested by the customer.

###

Example 14:

3	Shipowner	The shipowner updates the description and (or) the note fields and presses the "Save" button.

Split:
3	Shipowner	The shipowner updates the description and (or) the note fields.
3	Shipowner	The shipowner presses the "Save" button.

###
"""

USER_SPLIT="""{uc}

Split:"""

SYSTEM_COSMIC_MEASURE="""FP “Enquire on a Professor’s details”: 
1. When a Registrar wishes to enquire on the details of a Professor, he must first select the sub-option ‘Enquire on a Professor’. 
2. Then, he must enter the Professor ID. 
3. C-Reg searches for a Professor with the specified ID.
4. C-Reg displays a page (a form) with the Professor’s name and address, and other details. 
4. If a Professor with the specified ID is not found, C-Reg displays an error message, "Professor Not Found." 
5. The Registrar can then type in a different ID or cancel the operation.
6. If the Professor ID provided is not valid, C-Reg displays an error message, "Invalid Professor ID."

FP “Enquire on a Professor’s details” measurement:
Triggering Event: The Registrar selects the sub-option ‘Enquire on a Professor’
Functional User: Registrar
Sub-Processes:
1. When a Registrar wishes to enquire on the details of a Professor, he must first select the sub-option ‘Enquire on a Professor’. 
    No data movement.
2. Then, he must enter the Professor ID. 
    FU (Registrar) – DG (Professor ID) – OOI (Professor) – Entry
3. C-Reg searches for a Professor with the specified ID. 
    DG (Professor ID) – OOI (Professor) – Read.
4. C-Reg displays a page (a form) with the Professor’s name and address, and other details.
    DG (Professor details) – OOI (Professor) – Exit.
5. If a Professor with the specified ID is not found, C-Reg displays an error message, "Professor Not Found." 
    DG (Messages) – OOI (Message) – Exit. It must be counted only once.
6. The Registrar can then type in a different ID or cancel the operation.
    No data movement.
7. If the Professor ID provided is not valid, C-Reg displays an error message, "Invalid Professor ID."
    DG (Messages) – OOI (Message) – Exit. It must be counted only once.

###

FP “Add a Professor’s details”:
MAIN SCENARIO:
1. When a Registrar wishes to enter data about a new Professor, he selects the sub-option 'Add Professor'.
2. C-Reg displays a blank formatted screen for entry of Professor data.
3. The Registrar enters the following details for the Professor: ID, name and address, social security number, Department, qualifications and 
contact details.
4. The Registrar presses ‘Save’.
5. C-Reg validates the data to ensure the proper formats.
6. C-Reg checks if the social security number is greater than 0.
7. C-Reg checks whether a Professor of that ID already exists.
8. C-Reg creates a record for the new Professor.
9. C-Reg displays a confirmation message.

Alternative scenario no. 1:
1. If data entered is not valid, C-Reg displays one or more error messages, for example: ‘Professor ID unknown’, Professor name already 
exists’, "Professor Data Invalid".
2. The Registrar changes or corrects the data or modifies the fields properly.
3. The Registrar presses ‘Save’ again, or cancel the operation.

Alternative scenario no. 2:
1. The Registrar repeats the first 5 steps for each Professor that the Registrar wishes to add to C-Reg. 

FP “Add a Professor’s details” measurement:
Triggering Event: The Registrar selects the sub-option "Add Professor."
Functional User: Registrar
Sub-Processes:
MAIN SCENARIO:
1. When a Registrar wishes to enter data about a new Professor, he selects the sub-option 'Add Professor'.
    No data movement.
2. C-Reg displays a blank formatted screen for entry of Professor data.
    No data movement.
3. The Registrar enters the following details for the Professor: ID, name and address, social security number, Department, qualifications and 
contact details.
    FU (Registrar) - DG (Professor details) – OOI (Professor) – Entry.
4. The Registrar presses ‘Save’.
    No data movement.
5. C-Reg validates the data to ensure the proper formats.
    No data movement.
6. C-Reg checks if the social security number is greater than 0.
    No data movement.
7. C-Reg checks whether a Professor of that ID already exists.
    DG (Professor ID) – OOI (Professor) – Read.
8. C-Reg creates a record for the new Professor.
    DG (Professor details) – OOI (Professor) – Write.
9. C-Reg displays a confirmation message.
    DG (Messages) – OOI (Message) – Exit. It must be counted only once.

Alternative scenario no. 1:
1. If data entered is not valid, C-Reg displays one or more error messages, for example: ‘Professor ID unknown’, Professor name already 
exists’, "Professor Data Invalid".
    DG (Messages) – OOI (Message) – Exit. It must be counted only once.
2. The Registrar changes or corrects the data or modifies the fields properly.
    No data movement.
3. The Registrar presses ‘Save’ again, or cancel the operation.
    No data movement.

Alternative scenario no. 2:
1. The Registrar repeats the first 5 steps for each Professor that the Registrar wishes to add to C-Reg. 
    No data movement.

###

FP “Delete a Professor’s details”:
MAIN SCENARIO:
1. The Registrar presses ‘Delete’ relating to the Professor of his (or her) interest.
2. C-Reg enquires on the Course Catalog whether the Professor has any Course Offerings that he has committed to teach. 
3. The Course Catalog replies to C-Reg with a ‘yes/no’ indication.
4. If the Professor has no Course Offering teaching commitments, C-Reg displays a message asking
the Registrar to confirm the deletion.
5. If the Registrar selects ‘yes’, C-Reg deletes the Professor data.

Alternative flow no. 1:
6. if the Registrar selects ‘no’, the operation is cancelled.

Exceptions:
7. If the Professor is committed to teach any Course Offerings, deletion is not allowed, C-Reg displays an error message.
8. The Registrar must abandon the operation.

FP “Delete a Professor’s details” measurement:
Triggering Event: The Registrar presses ‘Delete’ relating to the Professor of his (or her) interest.
Functional User: Registrar
Sub-Processes:
MAIN SCENARIO:
1. The Registrar presses ‘Delete’ relating to the Professor of his (or her) interest.
    FU (Registrar) - DG (Professor ID) – OOI (Professor) – Entry.
2. C-Reg enquires on the Course Catalog whether the Professor has any Course Offerings that he has committed to teach. 
    FU (Course Catalog) - DG (Professor ID) – OOI (Professor) – Exit.
3. The Course Catalog replies to C-Reg with a ‘yes/no’ indication.
    FU (Course Catalog) - DG (Professor’s Course Offering) – OOI (Course Offerings) - Entry.
4. If the Professor has no Course Offering teaching commitments, C-Reg displays a message asking
the Registrar to confirm the deletion.
    No data movement.
5. If the Registrar selects ‘yes’, C-Reg deletes the Professor data.
    DG (Professor details) – OOI (Professor) – Write.

Alternative flow no. 1:
6. if the Registrar selects ‘no’, the operation is cancelled.
    No data movement.

Exceptions:
7. If the Professor is committed to teach any Course Offerings, deletion is not allowed, C-Reg displays an error message.
    DG (Messages) – OOI (Message) – Exit. It must be counted only once.
8. The Registrar must abandon the operation.
    No data movement.
 
###

FP “Search for ships”:
MAIN SCENARIO:
1. The system timer ticks.
2. The actor presses the “view ships” link to list all the ships.
3. The system searches for all the ships in persistent storage.
4. The system deletes the previously rented ship.
5. The system displays the list of the ships.
6. The actor clicks "Transform" relating to the ship of his interest.
7. The system requests the Sep service to process the transformation.
8. The Sep service replies with the transformation.

FP: "Search for ships" measurement:
Triggering Event: The system timer ticks.
Functional User: system timer
Sub-Processes:
MAIN SCENARIO:
1. The system timer ticks.
    FU (system timer) - DG (Clock tick) - OOI (Clock) - Entry.
2. The actor presses the “view ships” link to list all the ships.
    FU (actor) - DG (All ships) - OOI (Ship) - Entry.
3. The system searches for all the ships in persistent storage.
    DG (Ships details) - OOI (Ship) - Read.
4. The system deletes the previously rented ship.
    DG (Rented ships) - OOI (Ship) - Write.
5. The system displays the list of the ships.
    DG (Ships details) - OOI (Ship) - Exit.
6. The actor clicks "Transform" relating to the ship of his interest.
    FU (actor) - DG (Ship ID) - OOI (Ship) - Entry.
7. The system requests the Sep service to process the transformation.
    DG (Transformation) - OOI (Ship) - Exit.
8. The Sep service replies with the transformation.
    FU (Sep) - DG (Transformation) - OOI (Ship) - Entry.

###

FP “Reserve cabins”:
MAIN SCENARIO:
1	Operator	The actor presses "Reserve cabins" relating to the cabins of his interest.
2	System	The system stores the reserved cabins.
3	System	The system shows a confirmation message.

Alternative flow no. 1
1.a1	Operator	The user specifies the number of cabins.
2.a1	System	The system present static drop-down lists to specify every cabin's seat. The flow of events resumes at step no. 1 of the main scenario.

FP: "Reserve cabins" measurement:
Triggering Event: The actor presses "Reserve cabins" relating to the cabins of his interest.
Functional User: Operator
Sub-Processes:
MAIN SCENARIO:
1	Operator	The actor presses "Reserve cabins" relating to the cabins of his interest.
    FU (Operator) - DG (Reservation details) - OOI (Reservation) - Entry.
2	System	The system stores the reserved cabins.
    DG (Booked cabin details) - OOI (Booked cabin) - Write.
3	System	The system shows a confirmation message.
    DG (Messages) – OOI (Message) – Exit. It must be counted only once.

Alternative flow no. 1
1.a1	Operator	The user specifies the number of cabins.
    No data movement.
2.a1	System	The system present static drop-down lists to specify every cabin's seat. The flow of events resumes at step no. 1 of the main scenario.
    No data movement.

###

FP “Activate sensors”:
MAIN SCENARIO:
1.	Switch	The switch enters the "activate sensor" regarding a specific sensor.
2.	System	The system read the Sensor internal state.
3.	Sensor	The system requests the Sensor to process the "activate" command.
4.	Monitor	The Monitor displays the new Sensor state.

FP: "Activate sensors" measurement:
Triggering Event: The switch enters the "activate sensor" regarding a specific sensor.
Functional User: Switch
Sub-Processes:
MAIN SCENARIO:
1.	Switch	The switch enters the "activate sensor" regarding a specific sensor.
    FU (Switch) - DG (Activate signal) - OOI (Sensor) - Entry.
2.	System	The system read the Sensor internal state.
    DG (Sensor internal state) - OOI (Sensor) - Read.
3.	Sensor	The system requests the Sensor to process the "activate" command.
    FU (Sensor) - DG (Sensor internal state) - OOI (Sensor) - Exit.
4.	Monitor	The Monitor displays the new Sensor state.
    FU (Monitor) - DG (Sensor state) - OOI (Sensor) - Exit.

###

FP “Activate processes”:
MAIN SCENARIO:
1.	BG Process	The BG process sends the run command to the system.
2.	System	The system responds sending the "stop" command to the OS Process.
3.	System	The system sends the "stop" command to the SX Process.

FP: "Activate processes" measurement:
Triggering Event: The BG process sends the run command to the system.
Functional User: BG Process
Sub-Processes:
MAIN SCENARIO:
1.	BG Process	The BG process sends the run command to the system.
    FU (BG Process) - DG (Run command) - OOI (BG Process) - Entry.
2.	System	The system responds sending the "stop" command to the OS Process.
    FU (OS Process) - DG (Stop command) - OOI (OS Process) - Exit.
3.	System	The system sends the "stop" command to the SX Process.
    FU (SX Process) - DG (Stop command) - OOI (SX Process) - Exit.

###

"""

USER_COSMIC_MEASURE="""FP "{uc_name}":
{uc}

FP: "uc_name" measurement:"""
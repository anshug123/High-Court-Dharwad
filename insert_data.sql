-- judges table
INSERT INTO Courts (Court_ID, Court_Name, Location)
VALUES
    (101, 'Central District Court', 'New York'),
    (201, 'Northern Circuit Court', 'Chicago'),
    (301, 'Southern Superior Court', 'Los Angeles'),
    (401, 'Eastern Municipal Court', 'Miami'),
    (501, 'Western Circuit Court', 'Houston'),
    (601, 'Northern Superior Court', 'San Francisco'),
    (701, 'Eastern District Court', 'Atlanta'),
    (801, 'Western Municipal Court', 'Dallas'),
    (901, 'Southern Circuit Court', 'Seattle'),
    (1001, 'Central Municipal Court', 'Boston'),
    (1101, 'Northern Municipal Court', 'Philadelphia'),
    (1201, 'Eastern Circuit Court', 'Denver');


--  Judges table
INSERT INTO Judges (Judge_ID, Name, Age, Gender, Contact_Number, Address, Court_ID)
VALUES
    (111, 'John Smith', 45, 'Male', '1234567890', '123 Main St, New York', 101),
    (211, 'Jane Doe', 50, 'Female', '9876543210', '456 Elm St, Chicago', 201),
    (311, 'Robert Johnson', 55, 'Male', '5555555555', '789 Oak St, Los Angeles', 301),
    (411, 'Susan White', 48, 'Female', '1234567891', '456 Elm St, New York', 401),
    (511, 'Michael Johnson', 52, 'Male', '9876543211', '789 Oak St, Miami', 501),
    (611, 'Karen Davis', 49, 'Female', '5555555551', '234 Pine St, San Francisco', 601),
    (711, 'Richard Wilson', 47, 'Male', '1234567892', '101 Cedar St, Houston', 701),
    (811, 'Amanda Lee', 42, 'Female', '9876543212', '202 Birch St, Dallas', 801),
    (911, 'Daniel Brown', 56, 'Male', '5555555552', '303 Oak St, Atlanta', 901),
    (1011, 'Patricia Taylor', 51, 'Female', '1234567893', '404 Maple St, Boston', 901),
    (1111, 'Christopher Anderson', 44, 'Male', '9876543213', '505 Pine St, Seattle', 1101),
    (1211, 'Laura Martinez', 53, 'Female', '5555555553', '606 Elm St, Miami', 1101);

-- Add more judges here...

--  Cases table
INSERT INTO Cases (Case_ID, Case_Type, Filing_Date, Status, Judge_ID, Court_ID)
VALUES
    (1, 'criminal', '2023-01-15', 'pending', 111, 101),
    (2, 'civil', '2023-02-20', 'running', 211, 201),
    (3, 'criminal', '2023-03-10', 'end', 311, 301),
    (4, 'civil', '2023-04-01', 'pending', 411, 401),
    (5, 'criminal', '2023-05-15', 'running', 511, 501),
    (6, 'civil', '2023-06-20', 'end', 611, 601),
    (7,'civil','2023-07-25','pending',711,601),
    (8,'criminal','2023-07-10','end',811,801),
    (9,'criminal','2023-08-29','running',911,801),
    (10,'civil','2023-09-16','end',1011,1001),
    (11,'criminal','2023-08-29','running',1111,1101),
    (12,'civil','2023-10-09','pending',1211,1201);
-- Add more cases here...



--  lawyers table
INSERT INTO Lawyers (Lawyer_ID, Name, Age, Gender, Contact_Number, Address)
VALUES
    (120, 'Michael Brown', 40, 'Male', '1112223333', '789 Pine St, New York'),
    (220, 'Sarah Davis', 35, 'Female', '4445556666', '234 Cedar St, Chicago'),
    (320, 'Daniel Wilson', 45, 'Male', '7778889999', '567 Maple St, Los Angeles'),
    (420, 'Jennifer Lee', 38, 'Female', '1112223332', '789 Elm St, Miami'),
    (520, 'Robert Smith', 37, 'Male', '4445556662', '123 Cedar St, Houston'),
    (620, 'Sophia Martinez', 43, 'Female', '7778889992', '567 Oak St, San Francisco'),
    (720, 'Matthew Johnson', 41, 'Male', '1112223334', '345 Pine St, Dallas'),
    (820, 'Olivia Wilson', 36, 'Female', '4445556667', '456 Birch St, Philadelphia'),
    (920, 'David Miller', 44, 'Male', '7778889998', '678 Cedar St, Seattle'),
    (1020, 'Emma Moore', 39, 'Female', '1112223335', '789 Maple St, Boston'),
    (1120, 'William Davis', 42, 'Male', '4445556668', '890 Oak St, Denver'),
    (1220, 'Ava Taylor', 37, 'Female', '7778889997', '901 Elm St, Los Angeles');
-- Add more lawyers here...



--  Clients table
INSERT INTO Clients (Client_ID, Name, Age, Gender, Contact_Number, Address)
VALUES
    (1, 'Emily Johnson', 30, 'Female', '3334445555', '890 Spruce St, New York'),
    (2, 'William Smith', 28, 'Male', '6667778888', '123 Birch St, Chicago'),
    (3, 'Olivia White', 32, 'Female', '9990001111', '456 Oak St, Los Angeles'),
    (4, 'William Johnson', 28, 'Male', '6667778888', '234 Birch St, New York'),
    (5, 'Ella Brown', 35, 'Female', '5554443333', '890 Maple St, Miami'),
    (6, 'James Wilson', 32, 'Male', '9991112222', '456 Pine St, San Francisco'),
    (7, 'Sophia Davis', 29, 'Female', '1112223333', '789 Elm St, Chicago'),
    (8, 'Aiden Johnson', 27, 'Male', '5556667777', '345 Cedar St, Los Angeles'),
    (9, 'Ava Smith', 31, 'Female', '8889990000', '567 Oak St, Miami'),
    (10, 'Liam Wilson', 28, 'Male', '2223334444', '123 Maple St, New York'),
    (11, 'Oliver Brown', 33, 'Male', '6665554444', '456 Birch St, Chicago'),
    (12, 'Emma Lee', 30, 'Female', '9991112222', '890 Pine St, San Francisco');
-- Add more clients here...



--  ClientsCases table
INSERT INTO ClientsCases (ClientCase_ID, Client_ID, Case_ID)
VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5),
    (6, 6, 6),
    (7, 1, 2);
-- Add more client-case relationships here...



--  CaseLawyers table
INSERT INTO CaseLawyers (CaseLawyer_ID, Case_ID, Lawyer_ID)
VALUES
    (1, 1, 120),
    (2, 2, 220),
    (3, 3, 320),
    (4, 4, 420),
    (5, 5, 520),
    (6, 6, 620),
    (7, 6, 720),
    (8, 5, 820),
    (9, 6, 920),
    (10,7, 920);



-- Add more case-lawyer relationships here...

--  InvestigatingOfficers table
INSERT INTO InvestigatingOfficers (Officer_ID, Name, Age, Gender, Contact_Number)
VALUES
    (1, 'David Johnson', 42, 'Male', '2223334444'),
    (2, 'Mary Wilson', 38, 'Female', '7777777777'),
    (3, 'James Brown', 41, 'Male', '8888888888'),
    (4, 'Maria Johnson', 40, 'Female', '3334445555'),
    (5, 'John Wilson', 45, 'Male', '6669998888'),
    (6, 'Laura Davis', 39, 'Female', '1113332222'),
    (7, 'William Smith', 43, 'Male', '5556664444'),
    (8, 'Sophia Johnson', 37, 'Female', '7777771111'),
    (9, 'Daniel Wilson', 44, 'Male', '8888883333'),
    (10, 'Olivia Davis', 42, 'Female', '3335552222'),
    (11, 'Michael Brown', 46, 'Male', '6664447777'),
    (12, 'Ella Johnson', 40, 'Female', '1113336666');
-- Add more investigating officers here...



-- case_officers table
INSERT INTO CaseOfficers (CaseOfficer_ID, Case_ID, Officer_ID)
VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5),
    (6, 6, 6),
    (7, 6, 7),
    (8, 6, 8),
    (9, 6, 9),
    (10, 7, 10),
    (11, 8, 11),
    (12, 9, 11);
-- Add more case-officer relationships here...

--  Evidence table
INSERT INTO Evidence (Evidence_ID, Case_ID, Description, Type)
VALUES
    (1, 1, 'Weapon found at the crime scene', 'real'),
    (2, 2, 'Contract document', 'documentary'),
    (3, 3, 'Surveillance video footage', 'digital'),
    (4, 4, 'Fingerprint analysis report', 'documentary'),
    (5, 5, 'Crime scene photographs', 'real'),
    (6, 6, 'Witness testimonies', 'testimonial'),
    (7, 6, 'Email correspondence', 'documentary'),
    (8, 6, 'DNA test results', 'testimonial'),
    (9, 9, 'Security camera footage', 'digital'),
    (10, 10, 'Audio recording', 'documentary'),
    (11, 11, 'Physical weapon', 'real'),
    (12, 12, 'Expert witness report', 'testimonial');
-- Add more evidence entries here...

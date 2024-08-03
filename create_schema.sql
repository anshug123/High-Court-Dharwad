drop DATABASE highcourt;
CREATE DATABASE highcourt;
\c highcourt

-- Court
CREATE TABLE Courts (
    Court_ID INT PRIMARY KEY,
    Court_Name VARCHAR(50),
    Location VARCHAR(100),
    CHECK (Court_ID BETWEEN 1 AND 1300)
);

-- judges
CREATE TABLE Judges (
    Judge_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    Contact_Number VARCHAR(15),
    Address VARCHAR(100),
    Court_ID INT,
    FOREIGN KEY (Court_ID) REFERENCES Courts(Court_ID) ON DELETE CASCADE,
    CHECK (LENGTH(Contact_Number) = 10)
);

-- cases
CREATE TABLE Cases (
    Case_ID INT PRIMARY KEY,
    Case_Type VARCHAR(50),
    Filing_Date DATE,
    Status VARCHAR(20),
    Judge_ID INT,
    Court_ID INT,
    FOREIGN KEY (Judge_ID) REFERENCES Judges(Judge_ID) ON DELETE CASCADE,
    FOREIGN KEY (Court_ID) REFERENCES Courts(Court_ID) ON DELETE CASCADE,
    CHECK (Case_Type IN ('criminal', 'civil') AND Status IN ('pending', 'running', 'end'))
);

-- lawyers

CREATE TABLE Lawyers (
    Lawyer_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    Contact_Number VARCHAR(15),
    Address VARCHAR(100),
    CHECK (LENGTH(Contact_Number) = 10)
);

-- clients
CREATE TABLE Clients (
    Client_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    Contact_Number VARCHAR(15),
    Address VARCHAR(100),
    CHECK (LENGTH(Contact_Number) = 10)
);

-- client of cases

CREATE TABLE ClientsCases (
    ClientCase_ID INT PRIMARY KEY,
    Client_ID INT,
    Case_ID INT,
    FOREIGN KEY (Client_ID) REFERENCES Clients(Client_ID) ON DELETE CASCADE,
    FOREIGN KEY (Case_ID) REFERENCES Cases(Case_ID) ON DELETE CASCADE
);

-- lawyer of cases

CREATE TABLE CaseLawyers (
    CaseLawyer_ID INT PRIMARY KEY,
    Case_ID INT,
    Lawyer_ID INT,
    FOREIGN KEY (Case_ID) REFERENCES Cases(Case_ID) ON DELETE CASCADE,
    FOREIGN KEY (Lawyer_ID) REFERENCES Lawyers(Lawyer_ID) ON DELETE CASCADE
);

-- officer

CREATE TABLE InvestigatingOfficers (
    Officer_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    Contact_Number VARCHAR(15),
    CHECK (LENGTH(Contact_Number) = 10)
);

-- officer of cases

CREATE TABLE CaseOfficers (
    CaseOfficer_ID INT PRIMARY KEY,
    Case_ID INT,
    Officer_ID INT,
    FOREIGN KEY (Case_ID) REFERENCES Cases(Case_ID) ON DELETE CASCADE,
    FOREIGN KEY (Officer_ID) REFERENCES InvestigatingOfficers(Officer_ID) ON DELETE CASCADE
);

-- evidence 

CREATE TABLE Evidence (
    Evidence_ID INT PRIMARY KEY,
    Case_ID INT,
    Description TEXT,
    Type VARCHAR(50),
    FOREIGN KEY (Case_ID) REFERENCES Cases(Case_ID) ON DELETE CASCADE,
    CHECK (Type IN ('real', 'documentary', 'demonstrative', 'testimonial', 'digital'))
);
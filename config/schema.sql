-- Drop tables if they exist
DROP TABLE IF EXISTS Cats;
DROP TABLE IF EXISTS Volunteers;
DROP TABLE IF EXISTS Deaths;
DROP TABLE IF EXISTS VetVisits;
DROP TABLE IF EXISTS LocationMoves;
DROP TABLE IF EXISTS Documents;
DROP TABLE IF EXISTS Adopters;

-- Create Cats table
CREATE TABLE Cats (
    CatID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Sex TEXT,
    Colour TEXT,
    Condition TEXT,
    Weight REAL,
    BirthDate DATE,
    FirstVax DATE,
    SecondVax DATE,
    SteriDue DATE,
    AdoptedDate DATE,
    ReceivedDate DATE NOT NULL,
    CurrentLocation TEXT NOT NULL,
    AdopterID INTEGER,
    FOREIGN KEY (AdopterID) REFERENCES Adopters(AdopterID)
);

-- Create Volunteers table
CREATE TABLE Volunteers (
    VolunteerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    Location TEXT NOT NULL
);

-- Create Deaths table
CREATE TABLE Deaths (
    DeathID INTEGER PRIMARY KEY AUTOINCREMENT,
    CatID INTEGER NOT NULL,
    CauseOfDeath TEXT,
    VetName TEXT,
    Date DATE NOT NULL,
    Location TEXT,
    FOREIGN KEY (CatID) REFERENCES Cats(CatID)
);

-- Create VetVisits table
CREATE TABLE VetVisits (
    VisitID INTEGER PRIMARY KEY AUTOINCREMENT,
    CatID INTEGER NOT NULL,
    Diagnosis TEXT,
    MedsPrescribed TEXT,
    Date DATE NOT NULL,
    FOREIGN KEY (CatID) REFERENCES Cats(CatID)
);

-- Create LocationMoves table
CREATE TABLE LocationMoves (
    MoveID INTEGER PRIMARY KEY AUTOINCREMENT,
    CatID INTEGER NOT NULL,
    FromLocation TEXT,
    ToLocation TEXT NOT NULL,
    Date DATE NOT NULL,
    FOREIGN KEY (CatID) REFERENCES Cats(CatID)
);

-- Create Documents table
CREATE TABLE Documents (
    DocID INTEGER PRIMARY KEY AUTOINCREMENT,
    Type TEXT NOT NULL,
    File TEXT NOT NULL
);

-- Create Adopters table
CREATE TABLE Adopters (
    AdopterID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Contact TEXT NOT NULL
);

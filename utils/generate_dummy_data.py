import sqlite3
import os
import random
from datetime import datetime, timedelta

# Path to the database file
db_path = os.path.join('instance', 'cats.db')

# Dummy data
volunteers = [
    ('alice', 'password123', 'Location A'),
    ('bob', 'password456', 'Location B'),
    ('carol', 'password789', 'Location C')
]

def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

adopters = [
    (f'John Doe{random_date(datetime(2020, 1, 1), datetime(2023, 6, 20))}', 'john@example.com'),
    (f'Jane Smith{random_date(datetime(2020, 1, 1), datetime(2023, 6, 20))}', 'jane@example.com'),
    (f'Emily Johnson{random_date(datetime(2020, 1, 1), datetime(2023, 6, 20))}', 'emily@example.com')
]

cats = [
    ('Whiskers', 'Female', 'Brown', 'Healthy', 4.5, '2020-01-01', '2020-03-01', '2020-04-01', '2021-01-01', None, '2020-01-01', 'Location A', None),
    ('Tom', 'Male', 'Gray', 'Injured', 5.2, '2019-06-15', '2019-08-15', '2019-09-15', '2020-06-15', None, '2019-06-15', 'Location B', None),
    ('Luna', 'Female', 'Black', 'Healthy', 3.8, '2021-05-20', '2021-07-20', '2021-08-20', '2022-05-20', None, '2021-05-20', 'Location C', None)
]

vet_visits = [
    ('Whiskers', 'Checkup', 'None', random_date(datetime(2020, 1, 1), datetime(2023, 6, 20)).strftime('%Y-%m-%d %H:%M:%S')),
    ('Tom', 'Injury Treatment', 'Antibiotics', random_date(datetime(2019, 6, 15), datetime(2023, 6, 20)).strftime('%Y-%m-%d %H:%M:%S')),
    ('Luna', 'Vaccination', 'Vaccine', random_date(datetime(2021, 5, 20), datetime(2023, 6, 20)).strftime('%Y-%m-%d %H:%M:%S'))
]

location_moves = [
    ('Whiskers', 'Location A', 'Location B', random_date(datetime(2020, 1, 1), datetime(2023, 6, 20)).strftime('%Y-%m-%d %H:%M:%S')),
    ('Tom', 'Location B', 'Location C', random_date(datetime(2019, 6, 15), datetime(2023, 6, 20)).strftime('%Y-%m-%d %H:%M:%S')),
    ('Luna', 'Location C', 'Location A', random_date(datetime(2021, 5, 20), datetime(2023, 6, 20)).strftime('%Y-%m-%d %H:%M:%S'))
]

documents = [
    ('Vaccination Record', 'vaccination_record.pdf'),
    ('Adoption Agreement', 'adoption_agreement.pdf')
]

deaths = [
    ('Tom', 'Accident', 'Dr. Brown', random_date(datetime(2019, 6, 15), datetime(2023, 6, 20)).strftime('%Y-%m-%d %H:%M:%S'), 'Location C')
]

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Clear existing data
tables = ['Volunteers', 'Adopters', 'Cats', 'VetVisits', 'LocationMoves', 'Documents', 'Deaths']
for table in tables:
    cur.execute(f'DELETE FROM {table}')

# Insert dummy data into Volunteers
cur.executemany('''
    INSERT INTO Volunteers (Username, Password, Location) VALUES (?, ?, ?)
''', volunteers)

# Insert dummy data into Adopters
cur.executemany('''
    INSERT INTO Adopters (Name, Contact) VALUES (?, ?)
''', adopters)

# Insert dummy data into Cats
for cat in cats:
    cur.execute('''
        INSERT INTO Cats (Name, Sex, Colour, Condition, Weight, BirthDate, FirstVax, SecondVax, SteriDue, AdoptedDate, ReceivedDate, CurrentLocation, AdopterID)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', cat)

# Insert dummy data into VetVisits
cur.executemany('''
    INSERT INTO VetVisits (CatID, Diagnosis, MedsPrescribed, Date)
    SELECT CatID, ?, ?, ? FROM Cats WHERE Name = ?
''', [(diagnosis, meds, date, name) for name, diagnosis, meds, date in vet_visits])

# Insert dummy data into LocationMoves
cur.executemany('''
    INSERT INTO LocationMoves (CatID, FromLocation, ToLocation, Date)
    SELECT CatID, ?, ?, ? FROM Cats WHERE Name = ?
''', [(from_loc, to_loc, date, name) for name, from_loc, to_loc, date in location_moves])

# Insert dummy data into Documents
cur.executemany('''
    INSERT INTO Documents (Type, File) VALUES (?, ?)
''', documents)

# Insert dummy data into Deaths
cur.executemany('''
    INSERT INTO Deaths (CatID, CauseOfDeath, VetName, Date, Location)
    SELECT CatID, ?, ?, ?, ? FROM Cats WHERE Name = ?
''', [(cause, vet, date, loc, name) for name, cause, vet, date, loc in deaths])

# Commit changes and close the connection
conn.commit()
conn.close()

print("Dummy data inserted successfully")

import sqlite3
import time

# Connect or Create Database
db = sqlite3.connect("accounting.db")

def create_table():
    # Create Table
    db.execute('CREATE TABLE IF NOT EXISTS persons(name, surname, debt)')

def insert_person(name, surname, debt):
    # Insert person
    db.execute(f'INSERT INTO persons VALUES("{name}","{surname}", {debt})')
    db.commit()

def delete_person(name, surname):
    # Delete person
    db.execute(f'DELETE FROM persons WHERE name =  "{name}" and surname = "{surname}"')
    db.commit()

def show_persons():
    data = db.execute('SELECT * FROM persons')
    for name, surname, debt in data.fetchall():
        print(f"--------------\nName: {name} {surname}\nDebt: {debt}\n--------------")

def take_info():
    name = input("Enter a name: ")
    surname = input("Enter a surname: ")
    return name, surname

def update_person(name, surname, debt):
    db.execute(f"UPDATE persons SET debt = {debt} where name = {name} and surname = {surname}")
    db.commit()

def control_with_debt(name, surname, debt):
    if (name != "" and surname != "" and debt != ""):
        return True
    else:
        return False

def control(name, surname):
    if (name != "" and surname != ""):
        return True
    else:
        return False
def is_person_exists(name, surname):
    data = db.execute('SELECT * FROM persons')
    for db_name, db_surname, debt in data:
        if(db_name != name.upper() and db_surname != surname.upper()):
            return False
        else:
            return True

create_table()
while True:
    process = input(
        'Select your process:\n1) Add Person\n2) Delete Person\n3) Show Persons\n4) Update Person\n5) Exit\n--> ')
    if process == "5":
        print("---Exit---")
        break

    elif process == "1":
        name, surname = take_info()
        debt = input("Enter debt amount: ")
        if control_with_debt(name, surname, debt):
            if is_person_exists(name, surname):
                print("Person has already exist.")
            else:
                insert_person(name.upper(), surname.upper(), debt)
                print("\n---Person has added.---\n")
        else:
            print("\n!!! Invalid process. Try Again...\n")


    elif process == "2":
        name, surname = take_info()
        if control(name, surname) and is_person_exists(name, surname):
            delete_person(name, surname)
            print("\n---Person has deleted.---\n")
        else:
            print("\n!!! Invalid process. Try Again...\n")

    elif process == "3":
        show_persons()
        time.sleep(5)
        print("\n")

    elif process == "4":
        name, surname = take_info()
        debt = input("Enter new debt amount: ")
        control_with_debt(name, surname, debt)
        if control_with_debt(name, surname, debt) and is_person_exists(name, surname):
            update_person(name.upper(), surname.upper(), debt)
            print("\n---Person has updated.---\n")
        else:
            print("\n!!! Invalid process. Try Again...\n")



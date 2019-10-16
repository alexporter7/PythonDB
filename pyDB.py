#===============================================================================
# pyDB.py
#===============================================================================
# VERY basic way to interact with your database
# Quickly wrote it to be able to interact with MariaDB in UltraSeedBox
#
# This does not replace a full sql workbench but it does provide a way
# to quicly connect and show relevant information for what you are looking for
#===============================================================================
# Error Codes
# 1 - Could not find info.txt file in directory
# 2 - Could not connect to database
#===============================================================================

import mysql.connector

print("Opening info file")

try:
    file_name = "info.txt"
    file = open(file_name, 'r')

    h = file.readline() #host
    p = file.readline() #port
    u = file.readline() #user
    d = file.readline() #database

    h,p,u,d = h.replace("\n", ""), p.replace("\n", ""), u.replace("\n",""), d.replace("\n", "")

    print("File opened, variables are set")
except:
    print("File could not be found or open")
    exit_with_code(1)

print("Connecting to database")

pwd = input("Password>")

try:
    db = mysql.connector.connect(host=h,user=u,password=pwd,database=d, port=p)
    cur = db.cursor()
except:
    print("Could not connect to database")
    exit_with_code(2)

print("Connected to {}".format(h))

def log(text):
    pass

def exit_with_code(code):
    log(code)
    exit()

#============== SHOW TABLES ==============
def show_tables():
    arr = []
    cur.execute("SHOW TABLES")
    for x in cur:
        arr.append(x)

    print("======= TABLES =======")

    for o in arr:
        print(o)

#============== MENU ==============
def menu():
    command = input("{}/{}>".format(d, u))

    if command == "show":
        show_tables()
    elif command == "exit":
        exit_with_code(0)
    else:
        print(command)
        exit_with_code(0)

    menu()

menu()

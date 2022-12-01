import mysql.connector
from time import sleep

#mysql library --> Credentials um Datenbank zu verbinden
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
    database="rfid")
my_cursor = my_db.cursor()

# Log anlegen - Input:user_id
def write_log(user_id):
    sql = f'INSERT INTO logs (time_stamp,user_id) \
            VALUES (CURRENT_TIMESTAMP, {user_id});'
    my_cursor.execute(sql)
    my_db.commit()

# SQL-Select - Input:column, value return: [SQL-Ergebnis]
def db_single_select(column, value):
    sql = f'SELECT {column} FROM users WHERE {column} = {value};'
    my_cursor.execute(sql)
    select = my_cursor.fetchall()
    return select

# User anlegen - if Username+ID noch nicht in Datenbank return True; else False
def db_add_user(name, rfid):
    user_result = db_single_select('name', f'\'{name}\'')
    rfid_result = db_single_select('rfid', rfid)
    if len(user_result) == 0 and len(rfid_result) == 0:
        sql = f'INSERT INTO users (rfid, name) VALUES ({rfid}, \'{name}\');'
        my_cursor.execute(sql)
        my_db.commit()
        print("User", name, "registered.")
        sleep(2)
        return True
    elif len(user_result) > 0 and user_result[0][0] == name:
        print("User", name, "already in database registered.")
        sleep(2)
        return False
    elif len(rfid_result) > 0 and rfid_result[0][0] == rfid:
        print("RFID already in database registered.")
        sleep(2)
        return False

# Abfrage des usernames - input: userid return: username
def db_get_username(id):
    sql = f"SELECT name FROM users WHERE user_id = {id};"
    my_cursor.execute(sql)
    username = my_cursor.fetchall()
    return username[0][0]

# Abfrage der userid - input: rfid return: user_id
def db_get_user_id(rfid):
    sql = f"SELECT user_id FROM users WHERE rfid = {rfid};"
    my_cursor.execute(sql)
    user_id = my_cursor.fetchall()
    return user_id[0][0]

# User löschen - aus users und alle zugehörigen logs, sonst Integrity fail
def db_delete_user(id):
    if db_userid_check(id):
        name = db_get_username(id)
        sql = f"DELETE FROM logs WHERE user_id = {id};"
        my_cursor.execute(sql)
        my_db.commit()
        sql = f'DELETE FROM users WHERE user_id = {id};'
        my_cursor.execute(sql)
        my_db.commit()
        print("User", f'"{name}"', "ID:", id, "deleted.")
        sleep(2)

# User-exists check input user_id return: Bool
def db_userid_check(id):
    my_cursor.execute(f'SELECT user_id FROM users WHERE user_id={id};')
    result = my_cursor.fetchall()
    if len(result) == 0:
        print("UserID not in database")
        sleep(2)
        return False
    else:
        return True

# User aktivieren/deactivieren input: user_id
def db_de_or_activate_user(id):
    if db_userid_check(id):
        name = db_get_username(id)
        my_cursor.execute(f'SELECT active FROM users WHERE user_id={id};')
        result = my_cursor.fetchall()
        if result[0][0] == 1:
            my_cursor.execute(f'UPDATE users SET active=0 WHERE user_id={id};')
            my_db.commit()
            print("User", f'"{name}"', "User-ID:", id, "deactivated.")
            sleep(2)
        elif result[0][0] == 0:
            my_cursor.execute(f'UPDATE users SET active=1 WHERE user_id={id};')
            my_db.commit()
            print("User", f'"{name}"', "User-ID:", id, "activated.")
            sleep(2)

# User Authorisierung Input: RFID Output: Bool
def db_check(rfid):
    sql = f'SELECT user_id FROM users WHERE rfid={rfid};'
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    if len(result) == 1: # länge==1 heisst, dass der User in der DB vorhanden
        user_id = result[0][0]
        sql = f'SELECT name,active FROM users WHERE user_id = {user_id};'
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        if result[0][1] == 1: # check ob aktiv oder nicht
            print("Welcome ", db_get_username(user_id))
            write_log(user_id)
            return True
        else:
            print("User not authorized!")
            sleep(2)
    else:
        return False

from time import sleep
#import db_module
clear_console = lambda: print('\n' * 150)

def config():
    clear_console()
    x = input(
        ''' 
        ### RFID-Konfiguration ###

        (1) User anlegen
        (2) User löschen
        (3) User de-/aktivieren
        (4) Chip auslesen
        (5) User anzeigen
        (6) Logs anzeigen
        (7) Exit config
        (8) Quit

        Bitte Nummer eingeben:
        '''
    )
    if x == "1":
        try:
            while True:
                clear_console()
                print("### User anlegen ###\n")
                user_name = input("Bitte \"vorname_name\" eingeben: ").lower()
                rfid = int(reader())
                if db_module.db_add_user(user_name,rfid):
                    break
        except KeyboardInterrupt:
            return 0
        except:
            print("\nDatenbank-Probleme")
            sleep(1)
            return 0
    elif x == "2":
        try:
            clear_console()
            print("### User löschen ###\n(logs werden auch gelöscht)\n")
            userid = input("Bitte \"User-ID\" eingeben: ")
            db_module.db_delete_user(f'{userid}')
        except KeyboardInterrupt:
            return 0
        except:
            print("\nDatenbank-Probleme")
            sleep(1)
            return 0
    elif x == "3":
        try:
            clear_console()
            print("### User de-/aktivieren ###\n")
            userid = input("Bitte \"User-ID\" eingeben: ")
            db_module.db_de_or_activate_user(f'{userid}')
        except KeyboardInterrupt:
            return 0
        except:
            print("\nDatenbank-Probleme")
            sleep(1)
            return 0
    elif x == "4":
        clear_console()
        print("### Chip auslesen ###\n")
        try:
            rfid = reader()
        except:
            print("Reader offline")
            sleep(1)
            return 0
        try:
            userid = db_module.db_get_user_id(rfid)
        except:
            userid = 0
        if db_module.db_userid_check(userid):
            print("ChipID: ", rfid, "\nUsername:", db_module.db_get_username(userid))
        else:
            print("ChipID:", rfid, "Unregistered")
        input("\nPress Enter to continue:")
    elif x == "5":
        try:
            clear_console()
            sql = f'SELECT user_id,rfid,name,active FROM users;'
            db_module.my_cursor.execute(sql)
            result = db_module.my_cursor.fetchall()
            print("{:<10}{:<15}{:<25}{:^10}".format('User-ID', 'rfID', 'Username', '1=aktiv | 0=inaktiv'))
            for row in result:
                userid, rfid, name, aktiv = row
                print("{:<10}{:<15}{:<25}{:^10}".format(userid, rfid, name, aktiv))
            input("\nPress Enter to continue:")
        except KeyboardInterrupt:
            return 0
        except:
            print("\nDatenbank-Probleme")
            sleep(1)
            return 0
    elif x == "6":
        try:
            clear_console()
            sql = f'SELECT log_id,time_stamp,name FROM logs JOIN users ON logs.user_id=users.user_id \
                    WHERE log_id>(SELECT MAX(log_id) FROM logs)-40 ORDER BY time_stamp DESC;'
            db_module.my_cursor.execute(sql)
            result = db_module.my_cursor.fetchall()
            print("### die letzten 40 Log-Einträge werden angezeigt ###\n")
            print("{:<10}{:<25}{:<20}".format('Log-ID', 'Username', 'Timestamp'))
            for row in result:
                logid, timestamp, name = row
                print("{:<10}{:<25}{:%Y-%m-%d %H:%M:%S}".format(logid, name, timestamp))
            input("\nPress Enter to continue:")
        except:
            print("\nDatenbank-Probleme")
            sleep(1)
            return 0
    elif x == "7":
        clear_console()
        return(True)
    elif x == "8":
        clear_console()
        print("\nBye...")
        exit(0)
    else:
        clear_console()
        print("Keine korrekte Auswahl. \nBitte erneut versuchen.")
        sleep(1)

if __name__ == "__main__":
    run = True
    while True:
        try:
            try:
                while run == True:
                    clear_console()
                    open_door(db_module.db_check(reader()))
                while run == False:
                    run = config()
                    if run == True:
                        break
            except KeyboardInterrupt:
                if run == True:
                    run = False
                else:
                    break
        except Exception as error:
            print(error)

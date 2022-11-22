import db_module
import rfid_module
from time import sleep

clear_console = lambda: print('\n' * 150)
try:
    configrun = True
    while configrun:
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

            Bitte Nummer eingeben:
            '''
        )
        if x == "1":
            i = True
            while i:
                clear_console()
                print("### User anlegen ###\n")
                user_name = input("Bitte \"vorname_name\" eingeben: ").lower()
                rfid = int(rfid_module.reader())
                if db_module.db_add_user(user_name,rfid):
                    i = False
        elif x == "2":
            clear_console()
            print("### User löschen ###\n(logs werden auch gelöscht)\n")
            userid = input("Bitte \"User-ID\" eingeben: ")
            db_module.db_delete_user(f'{userid}')
        elif x == "3":
            clear_console()
            print("### User de-/aktivieren ###\n")
            userid = input("Bitte \"User-ID\" eingeben: ")
            db_module.db_de_or_activate_user(f'{userid}')
        elif x == "4":
            clear_console()
            print("### Chip auslesen ###\n")
            print(rfid_module.reader())
            input("\nPress Enter to continue:")
        elif x == "5":
            clear_console()
            sql = f'SELECT user_id,rfid,name,active FROM users;'
            db_module.my_cursor.execute(sql)
            result = db_module.my_cursor.fetchall()
            print("{:<10}{:<15}{:<25}{:^10}".format('User-ID', 'rfID', 'Username', '1=aktiv | 0=inaktiv'))
            for row in result:
                userid, rfid, name, aktiv = row
                print("{:<10}{:<15}{:<25}{:^10}".format(userid, rfid, name, aktiv))
            input("\nPress Enter to continue:")
        elif x == "6":
            clear_console()
            sql = f'SELECT log_id,time_stamp,name FROM logs JOIN users ON logs.user_id=users.user_id \
                    WHERE log_id>(SELECT MAX(log_id) FROM logs)-20 ORDER BY time_stamp DESC;'
            db_module.my_cursor.execute(sql)
            result = db_module.my_cursor.fetchall()
            print("{:<10}{:<25}{:<20}".format('Log-ID', 'Username', 'Timestamp'))
            for row in result:
                logid, timestamp, name = row
                print("{:<10}{:<25}{:%Y-%m-%d %H:%M:%S}".format(logid, name, timestamp))
            input("\nPress Enter to continue:")
        elif x == "7":
            clear_console()
            print("bye...")
            configrun = False
            break
        else:
            clear_console()
            print("Keine korrekte Auswahl. \nBitte erneut versuchen.")
            sleep(1)
except KeyboardInterrupt:
    exit(0)
except Exception as error:
    print(error)

from time import sleep
import db_module
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

clear_console = lambda: print('\n' * 150)

mfrc = SimpleMFRC522()

def reader():
    print("Chip vorhalten:")
    try:
        rfid, text = mfrc.read()
    finally:
        return rfid


def writer(text):
    try:
        mfrc.write(text)
        print("Chip registriert!")
        sleep(1)
    finally:
        return True

green_led = 3
relais = 5
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(relais, GPIO.OUT)


def open_door(authorized):
    if authorized:
        print("Sesam öffne dich!")
        GPIO.output(green_led, True)
        GPIO.output(relais, True)
        sleep(3)
        GPIO.output(green_led, False)
        GPIO.output(relais, False)
        # relais schalten + grüne LED
        # debug:
    else:
        # debug:
        print("Zugang verweigert!")


if __name__ == "__main__":
    while True:
        try:
            #clear_console()
            rfid = reader()
            open_door(db_module.db_check(rfid))
        except Exception as error:
            GPIO.cleanup()
            print(error)

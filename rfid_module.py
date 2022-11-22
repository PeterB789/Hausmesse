import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

mfrc = SimpleMFRC522()

def reader():
    print("Chip vorhalten:")
    try:
        rfid, text = mfrc.read()
    finally:
        GPIO.cleanup()
        return rfid


def writer(text):
    try:
        mfrc.write(text)
        print("Chip registriert!")
        sleep(1)
    finally:
        GPIO.cleanup()
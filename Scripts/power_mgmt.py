import RPi.GPIO as GPIO
from time import sleep
from subprocess import call

# Pin numbers (BCM numbering)
PIN_ACC = 27
PIN_LATCH = 25

INTERVAL = 10          # s
TIMEOUT_ACC_DOWN = 600 # s

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_ACC, GPIO.IN)
GPIO.setup(PIN_LATCH, GPIO.OUT, initial=GPIO.HIGH)

print("Latched power.")

acc_low_for_seconds = 0;

while True:
    sleep(INTERVAL)
    if GPIO.input(PIN_ACC) == 0:
        print("ACC low for " + str(acc_low_for_seconds) + " s")
        acc_low_for_seconds += INTERVAL
        if acc_low_for_seconds > TIMEOUT_ACC_DOWN:
            print("Powering off")
            call("sudo shutdown -h now", shell=True)
    else:
        acc_low_for_seconds = 0

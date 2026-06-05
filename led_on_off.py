import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 17

GPIO.setup(LED_PIN, GPIO.OUT)

print("LED on for 2 seconds...")
GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(2)

print("LED off.")
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()

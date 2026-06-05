import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 17
BUTTON_PIN = 27

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print("Press the button to turn the LED on. Ctrl+C to stop.")
    while True:
        button_state = GPIO.input(BUTTON_PIN)

        if button_state == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Stopping program...")

finally:
    GPIO.cleanup()

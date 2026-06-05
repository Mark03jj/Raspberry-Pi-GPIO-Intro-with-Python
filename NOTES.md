1 The easiest part was connecting the LED and resistor in series on the breadboard and also the required the most attention was making sure the GPIO pin, resister, LED, and ground were connected to the correct rows and pins.
2 The raspberry Pi GPIO pins operate at 3.3 V logic levels. Using higher voltages can damage the GPIO pins, so components connected to them should be designed to work safely with 3.3 V.
3 A resistor limits the amount of current flowing through the LED. Without it, too much current could flow, which could burn out the LED or potentially damage the Raspberry Pi.
4 The Raspberry Pi would try to control another GPIO pin than the one connected to the LED. As a result, the LED would not work as expected, or another connected device might be affected instead.
5 GPIO.cleanup() resets the GPIO pins that were used by the program back to their default state. This helps prevent conflicts or unexpected behavior when running future programs.

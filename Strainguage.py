import time
import RPi.GPIO as GPIO
from hx711py.hx711 import HX711

# Set up GPIO
GPIO.setmode(GPIO.BCM)
#test
# Create an instance of HX711 with GPIO pins for data and clock
hx = HX711(dout=25, pd_sck=24)

# Set up calibration factor (you might need to experiment with this value)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)

# Initialize the HX711
hx.reset()
hx.tare()

print("Start reading values from strain gauge")

# Continuously read values from the strain gauge
while True:
    try:
        weight = hx.get_weight(5)  # Take 5 readings and average
        print(f"Weight: {weight} grams")
        time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        break

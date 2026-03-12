# Night-Light
Using Raspberry Pi pico 2W to make a night light using led lights, HC-SR501 Pir Motion IR Sensor and a LM393 5MM LDR Photosensitive Sensor.

Connecting Motion Sensor
To connect the Motion Sensor to the Raspberry Pi pico 2w connect the VCC pin on the sensor to the VBUS pin on the Raspberry Pi pico 2W, and the ground to any ground on the Raspberry Pi pico 2W and the output sensor to any GP pins. On the code, motion_sensor = Pin(20, Pin.IN, Pin.PULL_DOWN)
change the 20 to whatever GP pin you used.

Connecting the Photosensitive Sensor
To connecct the Photosensitive sensor to the Raspberry Pi pico 2W connect the VCC pin to the 3V3_OUT pin on the Raspberry Pi pico 2W, and the ground to any ground on the Raspberry Pi pico 2W and the output sensor to any GP pins. On the code, light_sensor = Pin(16, Pin.IN), change 16 to what ever pin you are using.

NOTE PHOTOSENSITIVE SENSOR WILL NOT WORK IF YOU DON'T PLUG IT INTO THE 3V3_OUT PIN.

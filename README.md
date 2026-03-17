# Night-Light DOESN"T WORK AS OFF THIS MOMENT
Using Raspberry Pi pico 2W to make a night light using led lights, HC-SR501 Pir Motion IR Sensor and a LM393 5MM LDR Photosensitive Sensor.

Connecting Motion Sensor

<img width="351" height="274" alt="Screenshot 2026-03-11 at 23 28 56" src="https://github.com/user-attachments/assets/30b077fc-6c3b-43b5-8be2-af22f60492dd" />

To connect the Motion Sensor to the Raspberry Pi pico 2w connect the VCC pin on the sensor to the VBUS pin on the Raspberry Pi pico 2W, and the ground to any ground on the Raspberry Pi pico 2W and the output sensor to any GP pins. On the code, motion_sensor = Pin(20, Pin.IN, Pin.PULL_DOWN)
change the 20 to whatever GP pin you used.




Connecting the Photosensitive Sensor

<img width="269" height="213" alt="Screenshot 2026-03-11 at 23 27 38" src="https://github.com/user-attachments/assets/a4108023-18c9-437d-9531-36c20c4208ce" />

To connecct the Photosensitive sensor to the Raspberry Pi pico 2W connect the VCC pin to the 3V3_OUT pin on the Raspberry Pi pico 2W, and the ground to any ground on the Raspberry Pi pico 2W and the output sensor to any GP pins. On the code, light_sensor = Pin(16, Pin.IN), change 16 to what ever pin you are using.


NOTE:

PHOTOSENSITIVE SENSOR WILL NOT WORK IF YOU DON'T PLUG IT INTO THE 3V3_OUT PIN.

Some HC-SR501 Pir Motion IR Sensor comes with a plastic dome around the sensor, which might cause some miss readings, a recomendation is to remove the cover.

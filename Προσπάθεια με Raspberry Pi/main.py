from gpiozero import DistanceSensor, Buzzer
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17)
b = Buzzer(4)

while True:
    d = sensor.distance * 100
    print(d)
    if d < 20:
        b.beep(n=1)
    sleep(1)




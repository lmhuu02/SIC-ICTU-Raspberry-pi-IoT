'''
group 1: by Le Minh Huu @copyright
pr: control 3 led by sensor untrasonic
raspberry pi 4 - gpio zero
time: 23/7/2024 - ICTU
'''
from gpiozero import DistanceSensor
from time import sleep

# Khởi tạo các đối tượng LED với các chân GPIO tương ứng
ledRed = LED(21) #GPIO 21 PIN 40
LedGreen = LED(20) #GOIO 20 PIN 38
LedAmber = LED(16) #GPIO 16 pin 36

# Khởi tạo cảm biến với chân Echo nối vào GPIO23 và chân Trig nối vào GPIO24
sensor = DistanceSensor(echo=23, trigger=24)

while True:
    print(f"Khoảng cách: {sensor.distance * 100:.2f} cm")
    #dieu khien led
    # bat den do neu khoang cach nho hon 20 cm
    if sensor.distance * 100 <= 20:
        ledRed.on()        # Bật LED do
        LedGreen.off()       # Tắt LED xanh
        LedAmber.off()       # Tắt LED ho phach
        print("bat led red")                

    # bat den xanh neu khoang cach nho hon 80 cm
    elif sensor.distance * 100 >= 80:
        ledRed.off()        # tat LED do
        LedGreen.on()       # bat LED xanh
        LedAmber.off()       # Tắt LED ho phach
        print("bat led xanh") 

    # bat den ho phach neu khoang cach trong khoang 20 - 80 cm
    else:
        ledRed.off()        # tat LED do
        LedGreen.off()       # Tắt LED xanh
        LedAmber.on()       # bat LED ho phach
        print("bat led ho phach") 
    sleep(1)

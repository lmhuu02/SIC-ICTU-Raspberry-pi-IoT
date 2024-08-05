'''
group 1: by Le Minh Huu @copyright
pr: untrasonic and button on -> on srf sr-04 and control led, save log.txt
raspberry pi 4 - gpio zero
time: 5/7/2024 - ICTU
'''

#khai bao thu vien
from gpiozero import DistanceSensor, Button, LED
from datetime import datetime
import time

# Cấu hình cảm biến siêu âm, nút bấm và đèn LED
#NOTE: GPIO KHAC VOI PIN (40 pin) TREN PI
sensor = DistanceSensor(echo=24, trigger=23)
button = Button(25) #nut nhan duoc noi voi gnd
led = LED(20)   #led duoc noi chung am, dieu khien muc duong

# Đường dẫn tệp nhật ký
log_file_path = '/home/pi/Unit_Parctice/distance_log.txt'

# Ghi giá trị đo được vào tệp nhật ký
def log_distance(distance):
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{datetime.now()}: Distance is {distance} meters\n")

# Đo khoảng cách ban đầu
initial_distance = sensor.distance
print(f"Initial distance: {initial_distance:.2f} meters")

# Hàm đo khoảng cách khi nhấn nút
def measure_distance():
    print("nhan nut")
    current_distance = sensor.distance #doc cam bien sieu am
    log_distance(current_distance) #luu gia tri cam bien sieu am
    print(f"Measured distance: {current_distance:.2f} meters")
    
    # Bật đèn LED nếu khoảng cách nhỏ hơn khoảng cách ban đầu
    if current_distance < initial_distance:
        led.on()
        print("khoang cach nho hon: bat led")
    else:
        led.off()
        print("khoang cach lon hon: tat led")


# Chương trình chạy vô hạn để chờ nhấn nút
while True:
    #neu nut nhan duoc nhan thi se thuc hien do khoang cach lan sau dieu khien led
    if button.is_pressed:
        print("nhan nut")
        measure_distance()
        
    time.sleep(1)

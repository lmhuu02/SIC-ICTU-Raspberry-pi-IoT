'''
group 1: by Le Minh Huu @copyright
pr: control 3 led by 1 button
raspberry pi 4 - gpio zero
time: 23/7/2024 - ICTU
'''

#include thu vien
from gpiozero import LED, Button
from time import sleep


# Khởi tạo các đối tượng LED với các chân GPIO tương ứng
led1 = LED(21) #GPIO 21 PIN 40 led do
led2 = LED(20) #GOIO 20 PIN 38 led xanh
led3 = LED(16) #GPIO 16 pin 36 led ho phach

button = Button(12)
num = 0
# Chạy vòng lặp vô hạn để thực hiện các hành động điều khiển
while True:
    
    #dieu khien led
    if button.is_pressed:
        num = num + 1         
        if num > 3:
            num = 1
        button.wait_for_press()
        sleep(1)
        
    if num == 1:
        led1.on()        # Bật LED1
        led2.off()       # Tắt LED2
        led3.off()       # Tắt LED3
        print("bat led 1")        
        
    if num == 2:
        led1.off()        # tat LED1
        led2.on()       # bat LED2
        led3.off()       # Tắt LED3
        print("bat led 2")     
           
    if num == 3:
        led1.off()        # tat LED1
        led2.off()       # Tắt LED2
        led3.on()       # bat LED3
        print("bat led 3")

    sleep(0.5)

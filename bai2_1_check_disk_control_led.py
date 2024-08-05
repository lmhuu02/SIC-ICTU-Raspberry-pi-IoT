'''
group 1: by Le Minh Huu @copyright
pr: check disk if > 60 led red on, else led green on. save file log.txt
raspberry pi 4 - gpio zero
time: 5/7/2024 - ICTU
'''

#khai bao thu vien
import psutil
import time
from gpiozero import LED
from datetime import datetime

# Cấu hình đèn LED
red_led = LED(17)
yellow_led = LED(27)

# Đường dẫn tệp nhật ký
log_file_path = '/home/pi/Unit_Parctice/disk_usage_log.txt'

def log_disk_usage(usage):
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{datetime.now()}: Disk usage is {usage}%\n")

while True:
    # Lấy thông tin mức sử dụng đĩa
    disk_usage = psutil.disk_usage('/').percent
    
    # Điều khiển đèn LED dựa trên mức sử dụng đĩa
    if disk_usage > 60:
        red_led.on()
        yellow_led.off()
        print("disk > 60 -- bat led do")
    elif disk_usage > 30:
        yellow_led.on()
        red_led.off()
        log_disk_usage(disk_usage)
        print("disk > 30 -- bat led vang")
    else:
        red_led.off()
        yellow_led.off()
        print("disk < 30 -- tat led")

    log_disk_usage(disk_usage)

    # Chờ 1 phút trước khi kiểm tra lại
    time.sleep(60)

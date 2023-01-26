import subprocess
import time
print("******************************************")
print('Welcome to Frasha Santo\'s password viewer')
print("******************************************")
time.sleep(1)
t1 = subprocess.run(['netsh', 'wlan', 'show', 'profile'], text=True, capture_output=True).stdout
print(t1)
wifi_name = input("Enter the ssid of the wifi you want to know the password? ")

#Opening a file wifipass to store
with open('wifipass.txt', 'w') as wifipass:
    t2 = subprocess.run(['netsh', 'wlan', 'show', 'profile', wifi_name, 'key=clear'], capture_output=True, text=True).stdout
    wifipass.write(t2)
  
t3 = subprocess.run('type wifipass.txt | findstr Key ',shell = True, capture_output=True, text= True) 
print(f'Password: {t3.stdout}')
time.sleep(7)



  








    
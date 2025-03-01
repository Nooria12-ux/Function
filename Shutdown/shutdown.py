import os

shutdown = input("yo you wanna shutdown your computer? (yes or no): ")

if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")
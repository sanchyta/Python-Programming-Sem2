# Traffic police system (overspeeding)
"""
Created on Tue Feb 10 13:09:42 2026

@author: Sanchita Jadhav
"""

speed=int(input("Enter vehicle speed (km/h):"))
if speed>60:
    print("you are overspeeding.Fine will be charged.")
else:
    print("speed is within limit.")
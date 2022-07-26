import datetime
import os
import time 
import random 
import webbrowser 
from tkinter import messagebox 
from tkinter import *
import sys
root = Tk()

if not os.path.isfile("alarm_songs.txt"):
    print('Creating "alarm_songs.txt"...') 
    alarm_file = open("alarm_songs.txt", "w")

def check_alarm_input(alarm_time): 
    if len(alarm_time) == 1:
        if alarm_time[0] < 24 and alarm_time[0] >=0:
            return True 
    if len(alarm_time) == 2: 
        if alarm_time[0] < 24 and alarm_time[0] >=0 and alarm_time[1] < 60 and alarm_time[1] >=0: 
            return True 
    elif len(alarm_time) == 3: 
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0 and alarm_time[2] < 60 and alarm_time[2] >= 0: 
            return True 
    return False

def alarm():
    global alarm_time 

def snooze_duration(snooze_time):
    if check_alarm_input(alarm_time): 
        return True 
    return False

def ringtone(alarm_ringtone): 
    if check_alarm_input(alarm_time): 
        return True 
    return False

print("Set a time for the (ex. 6:30 or 18:30:00)") 
while True: 
    alarm_input = input(">> ") 
    try: 
        alarm_time = [int(n) for n in alarm_input.split(":")]
        if check_alarm_input(alarm_time): 
            break 
        else: 
            raise ValueError 
    except ValueError: 
        print("ERROR: Enter time in HH:MM or HH:MM:SS format") 
print ("What song would you like to play? Input a link here") 
while True: 
    song_input = input(">> ") 
    try: 
        with open("alarm_songs.txt", "w") as alarm_file:
            alarm_file.write(song_input)
            alarm_ringtone = song_input
        if ringtone(alarm_ringtone): 
            break 
        else:
            raise ValueError
    except ValueError: 
        print("ERROR: Enter a valid link")
    
then = datetime.datetime.now()
seconds_hms = [3600, 60, 1] 
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

now = datetime.datetime.now() 
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

time_diff_seconds = alarm_seconds - current_time_seconds 

if time_diff_seconds < 0: 
    time_diff_seconds += 86400

print ("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

time.sleep(time_diff_seconds)

print("Wake Up!")

with open("alarm_songs.txt", "r") as alarm_file: 
    videos = alarm_file.readlines() 

webbrowser.open(random.choice(videos))

Snoozing = True
while Snoozing:
    MSGBox = messagebox.askquestion("Alarm-Clock", "Your alarm is up! Snooze?", icon = "warning")
    if MSGBox == "yes": 
        print ("How long would you like to snooze? Express in minutes")
        snooze_time_input = input (">> ")
        snooze_time = float(snooze_time_input)
        time_diff_seconds_snooze = int(float(snooze_time)*60)
        print ("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds_snooze))
        time.sleep(time_diff_seconds_snooze)
        print ("Wake Up!")
        with open("alarm_songs.txt", "r") as alarm_file: 
            videos = alarm_file.readlines()   
        webbrowser.open(random.choice(videos))  
    else:
        root.destroy()
        sys.exit
        print ("Alarm off!")
        Snoozing = False

now  = datetime.datetime.now()                        
duration = now - then                         
duration_in_s = duration.total_seconds() 
hours = duration_in_s/3600
message = "You slept for: " + str(hours) + " hours"
print (message)
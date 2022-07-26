# Import needed packages
import datetime
import os
import time 
import random 
import webbrowser 
from tkinter import messagebox 
from tkinter import *
import sys
root = Tk()

# If the txt file that contains the song URL does not exist, this will automatically create it.
if not os.path.isfile("alarm_songs.txt"):
    print('Creating "alarm_songs.txt"...') 
    alarm_file = open("alarm_songs.txt", "w")

def check_alarm_input(alarm_time): 
    if len(alarm_time) == 1: # Alarm clock in [Hour] Format.
        if alarm_time[0] < 24 and alarm_time[0] >=0:
            return True 
    if len(alarm_time) == 2: # Alarm clock in [Hour:Minute] Format.
        if alarm_time[0] < 24 and alarm_time[0] >=0 and alarm_time[1] < 60 and alarm_time[1] >=0: 
            return True 
    elif len(alarm_time) == 3: # Alarm Clock in [Hour:Minute:Second] Format.
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0 and alarm_time[2] < 60 and alarm_time[2] >= 0: 
            return True 
    return False

# Function for alarm ringtone which will only function if the alarm input is valid.
def ringtone(alarm_ringtone): 
    if check_alarm_input(alarm_time): 
        return True 
    return False

# Gets user input for alarm.
print("Set your alarm (ex. 6:30 or 18:30:00)") 
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
# Gets user input for alarm song that is to be played when alarm goes off. 
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
    
then = datetime.datetime.now() # Marks the time when the alarm has started as a part of the duration of alarm feature of the alarm clock.

# Converts the alarm time to seconds.
seconds_hms = [3600, 60, 1] 
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# Converts the current time to seconds.
now = datetime.datetime.now() 
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

# The time (in seconds) before the alarm goes off.
time_diff_seconds = alarm_seconds - current_time_seconds 

# Signifies if the alarm is set at a time that has already passed during the current day. THis is will set an alarm for the next day.
if time_diff_seconds < 0: 
    time_diff_seconds += 86400 # Seconds in one day 

# Displays how long the alarm goes off.
print ("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

# Timer sleeps until the alarm goes off.
time.sleep(time_diff_seconds)

# Displayed when alarm goes off.
print("Wake Up!")

# Opens the chosen alarm song URL when alarm goes off.
with open("alarm_songs.txt", "r") as alarm_file: 
    videos = alarm_file.readlines() 

webbrowser.open(random.choice(videos))

# Snooze Function.
Snoozing = True
while Snoozing:
    MSGBox = messagebox.askquestion("Alarm-Clock", "Your alarm is up! Snooze?", icon = "warning") # Messagebox appears when alarm goes off to see if user wants to snooze the alarm.
    if MSGBox == "yes": 
        print ("How long would you like to snooze? Express in minutes")
        snooze_time_input = input (">> ") # User shall input how long they want the snooze to be.
        snooze_time = float(snooze_time_input)
        time_diff_seconds_snooze = int(float(snooze_time)*60)
        print ("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds_snooze)) # Displays the amount of time left before alarm goes off after snooze.
        time.sleep(time_diff_seconds_snooze) # Timer sleeps until snooze ends.
        print ("Wake Up!") # Displays when snooze ends.
        with open("alarm_songs.txt", "r") as alarm_file: # Opens the chosen alarm song URL when snooze goes off.
            videos = alarm_file.readlines()   
        webbrowser.open(random.choice(videos))  
    else:
        root.destroy()
        sys.exit
        print ("Alarm off!")
        Snoozing = False # Text box closes and alarm will end.
# Duration feature where it shows how long you "slept" (or how long the alarm lasted) expressed in minutes.
now  = datetime.datetime.now()                        
duration = now - then                         
duration_in_s = duration.total_seconds() 
hours = duration_in_s/3600
message = "You slept for: " + str(hours) + " hours"
print (message)
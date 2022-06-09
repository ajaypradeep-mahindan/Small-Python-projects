import time as manikuttan
#importing time packages as manikuttan
# function for time calculations 
def countdown(time_seconds):
  while time_seconds:
    mins,secs = divmod(time_seconds, 60)
    #minutes,seconds calculation
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    #minutes and seconds didplayed
    print(timeformat, end='\r')
    #ending of output in the form is given
    manikuttan.sleep(1)
    #sleeping python for 1 second
    time_seconds -= 1

print("stop")
#to stop the pythonmodule 
num=int(input("Set Your Timer in Sec : "))

countdown (num)
#giving the argument
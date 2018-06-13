minute = int(input('Minutes ==> '))
print(minute)
sec    = int(input('Seconds ==> '))
print(sec)
miles  = float(input('Miles ==> '))
print(miles,"\n")
s_to_min = sec/60
pace_in_min= ((s_to_min+minute)/miles)
pace_in_sec= ((s_to_min+minute)%(miles)/miles)*60
pace_min = (int(pace_in_min))
pace_sec = (int(pace_in_sec))

hour = minute/60+(s_to_min/60)
speed = round((miles/hour),2)

print("Pace is", pace_min, "minutes and", pace_sec,"seconds per mile.")
print("Speed is", speed, "miles per hour.")
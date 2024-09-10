t = int(input(""))
hours = t//60
mins = t%60

if hours<10:
    hrs_str = "0"+str(hours)
else:
    hrs_str = str(hours)

if mins<10:
    mins_str = "0"+str(mins)
else:
    mins_str = str(hours)

Time = hrs_str+":"+mins_str
print(Time)
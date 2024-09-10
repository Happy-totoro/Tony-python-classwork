hours = int(input(""))
mins = int(input(""))
T = input("")

if T == "am":
    clock = hours*60+mins
    print(clock)
elif T == "pm":
    clock = (hours+7)*60+mins
    print(clock)
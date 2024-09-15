lasttime = int(input("the car mileage the last time the car was filled:"))
now = int(input("the car mileage now:"))
amount = float(input("the total number of litres taken to fill the tank:"))

mileage_diff = now-lasttime

amount *= 0.22

answ = mileage_diff/amount

print("The car's miles per gallon is:", answ)
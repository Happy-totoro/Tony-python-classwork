Room_dimension = float(input("Room dimension:"))
Unpaintable_areas = float(input("Unpaintable areas:"))
coats = float(input("number of coats:"))

paint = (Room_dimension-Unpaintable_areas)*coats/11
print("The liter of paint you need to use:""%.2f"%paint+"L")
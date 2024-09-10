while True:
    password = input("")
    if len(password) < 8:
     print("The password needs to be at least 8 characters long")
    else:
       print("Your password has been changed to", password) 
       break
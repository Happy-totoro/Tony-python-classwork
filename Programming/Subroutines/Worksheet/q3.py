def getPword(attempt):
    attemt = int(input("'1' for enter a password, '2' for re-enter a password:"))
    if attempt == 1:
        pwrd = input("enter password:\n")
    elif attempt == 2:
        pwrd = input("re-enter the password:\n")
    while len(pwrd)<6 or len(pwrd)>8:
        print("Error. Password should be 6 to 8 characters long.")
        if attempt == 1:
            pwrd = input("enter password:\n")
        elif attempt == 2:
            pwrd = input("re-enter the password:\n")
    return pwrd
def main():
    pwrd1 = getPword(1)
    pwrd2 = getPword(2)
    while pwrd1 != pwrd2:
        print("Error. Password does not match.")
        pwrd1 = getPword(1) 
        pwrd2 = getPword(2)
    print("Password change sucessful.")
main()
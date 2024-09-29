def main():
    names = [None]*10
    count = 0
    while True:
        choice = display_menu()
        if choice == 1:
            count = add_name(names, count)
        elif choice == 2:
            display_list(names, count)
        elif choice == 3:
            print("Program terminating")
            break
        else:
            print("Invalid choice, please try again.")
def display_menu():
    print("1: Add name")
    print("2: Display list")
    print("3: Quit")
    choice = int(input("Enter your choice: "))
    return choice
def add_name(names, count):
    if count<10:
        name = input("Enter name to add: ")
        names[count] = name
        count +=1
    else:
        print("The list is full.")
    return count
def display_list(names, count):
    if count == 0:
        print("The list is empty.")
    else:
        for i in range(count):
            print(names[i])
main()
students = int(input("no. of students:"))
books = int(input("no. of books:"))

answ1 = books//students
answ2 = books%students

print("Each student will get", answ1, "books", "\nand", answ2, "books remaining")
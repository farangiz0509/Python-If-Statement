month = int(input("enter number of the month:"))

if month == 12 or month == 1 or month ==2:
    print("winter")
if month == 3 or month == 4 or month == 5:
    print("spring")
if month == 5 or month == 6 or month == 7:
    print("summer")
if month == 8 or month == 9 or month == 10:
    print("fall")
else:
    print("wrong number")
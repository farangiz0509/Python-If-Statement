a = int(input(" 1 tomonini kiriting"))
b = int(input("2 tomonini kiritig"))
c = int(input("3 tomonini kiriting"))

if a == b == c :
    print("teng tomonli")
if a == b or b == c or a == c:
    print("teng  yonli")
else:
    print("turli tomonli")
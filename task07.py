email = input("enter email:")

if "@" in email and "_" in email .split("@")[-1] and "" not in email:
    print("email is correct")
else:
    print("email is uncorrect")
d={1:10,2:20,3:30,4:40,5:50,6:60}

key=int(input("Enter the key whose value you want to find in the dictionary: "))
if key in d:
    print(f"The value of {key} is: {d[key]}")
else:
    print("Invalid input")
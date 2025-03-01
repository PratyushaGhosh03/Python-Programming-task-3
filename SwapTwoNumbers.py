# Get a three-digit number from the user
num = int(input("Enter a three-digit number: "))

# Check if the number is within the three-digit range
if 100 <= num <= 999:
    print(f"Multiplication Table of {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Please enter a valid three-digit number (100-999).")



# Get the number from the user
num = int(input("Enter a number: "))

# Print the multiplication table
print(f"Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


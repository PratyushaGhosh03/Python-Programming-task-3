# Get input from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary
binary_representation = bin(decimal_number)[2:]  # Removing '0b' prefix

# Display the result
print(f"Binary representation of {decimal_number} is: {binary_representation}")

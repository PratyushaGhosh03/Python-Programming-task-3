# Get matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize matrices
print("Enter elements for the first matrix:")
matrix1 = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

print("Enter elements for the second matrix:")
matrix2 = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

# Add the matrices
result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

# Display the result
print("Sum of the matrices:")
for row in result_matrix:
    print(row)

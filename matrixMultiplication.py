# Get matrix dimensions from the user
rows_A = int(input("Enter the number of rows for the first matrix: "))
cols_A = int(input("Enter the number of columns for the first matrix: "))

rows_B = int(input("Enter the number of rows for the second matrix: "))
cols_B = int(input("Enter the number of columns for the second matrix: "))

# Matrix multiplication condition: Columns of A must be equal to Rows of B
if cols_A != rows_B:
    print("Matrix multiplication not possible! Columns of A must equal rows of B.")
else:
    # Get first matrix
    print("Enter elements for the first matrix:")
    matrix_A = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols_A)] for i in range(rows_A)]

    # Get second matrix
    print("Enter elements for the second matrix:")
    matrix_B = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols_B)] for i in range(rows_B)]

    # Initialize result matrix with zeros
    result_matrix = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]

    # Display the result matrix
    print("Resultant Matrix after multiplication:")
    for row in result_matrix:
        print(row)

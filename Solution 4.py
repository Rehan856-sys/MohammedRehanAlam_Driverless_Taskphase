def matrix_multiply(A, B):

    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Error: Matrix multiplication is impossible.")
        return None

    result = []

    for i in range(rows_A):
        row = []

        for j in range(cols_B):
            total = 0

            for k in range(cols_A):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result



rows_A = int(input("Enter number of rows of A: "))
cols_A = int(input("Enter number of columns of A: "))

A = []

print("Enter elements of A:")
for i in range(rows_A):
    row = []
    for j in range(cols_A):
        value = int(input(f"A[{i}][{j}]: "))
        row.append(value)
    A.append(row)



rows_B = int(input("Enter number of rows of B: "))
cols_B = int(input("Enter number of columns of B: "))

B = []

print("Enter elements of B:")
for i in range(rows_B):
    row = []
    for j in range(cols_B):
        value = int(input(f"B[{i}][{j}]: "))
        row.append(value)
    B.append(row)


C = matrix_multiply(A, B)

if C is not None:
    print("Result:")
    for row in C:
        print(row)

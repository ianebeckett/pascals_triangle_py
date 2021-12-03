from math import factorial


# start by displaying the first six rows of Pascal's Triangle

# instead of checking the value of the previous entries, we can find the value of row n, column k by nCk(n,k),
# which is defined as n! / ((n-k)! * k!)
def combination(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))


# make the initial triangle
def generateTriangle(rows):
    print("\n")
    for row in range(rows):
        currentRow = [None] * (row + 1)
        for i in range(len(currentRow)):
            currentRow[i] = combination(row, i)
            currentRow[i] = str(currentRow[i])
        print((row * ' ').join(currentRow))  # FIXME improve the formatting to make diagonals more apparent
    print("\n")


def main():
    userRows = int(input("How many rows of Pascal's triangle would you like? Enter a number: "))
    generateTriangle(userRows)
    main()


main()

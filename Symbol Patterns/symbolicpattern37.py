print("Enter the no of rows: ")
n = int(input())
for i in range(0, n):
    for j in range(0, i+1):
        if i % 2 == 0:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()

for x in range(7):
    for y in range(5):
        print(end=" ")
        if (y == 0) or (y == 4 and (x != 0 and x != 3 and x != 6)) or ((x == 0 or x == 3 or x == 6) and (4 > y > 0)):
            print("*", end=" ")
        else:
            print(end="  ")
    print(" ")
print("\n")

for row in range(7):
    for col in range(5):
        print(end=" ")
        if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (4 > col > 0)):
            print("*", end="")
        else:
            print(end=" ")
    print(" ")
print("\n")

for row in range(7):
    for col in range(5):
        print(end=" ")
        if col == 0 or (col == 4 and (row != 0 and row != 3)) or ((row == 0 or row == 3) and (4 > col > 0)):
            print("*", end="")
        else:
            print(end=" ")
    print(" ")
print("\n")

for row in range(7):
    for col in range(5):
        print(end=" ")
        if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (4 > col > 0)):
            print("*", end="")
        else:
            print(end=" ")
    print(" ")
print("\n")

for row in range(7):
    for col in range(5):
        print(end=" ")
        if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (4 > col > 0)):
            print("*", end="")
        else:
            print(end=" ")
    print(" ")
print("\n")

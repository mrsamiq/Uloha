n = int(input("Zadaj vysku: "))

for r in range(n):
    for s in range(n):
        print("x", end="")
    print()

n = int(input("Zadaj sirku: "))

for r in range(n):
    for s in range(n):     
        if (r + s) % 2 == 0:
            print("x", end="")
        else:
            print(" ", end="")
    print()
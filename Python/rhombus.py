def pattern():
    n = int(input("Enter the height of the pattern : "))
    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print("", end = " ")
        print("*  "*5)
        print()

if __name__ == '__main__':
    pattern()

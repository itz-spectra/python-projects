N1 = input("Enter first number: ")
N2 = input("Enter second number: ")

while True:  
    W = input("""What Would you like to do:

    1. Plus
    2. Substract
    3. Multiply
    4. divide

    --> """)
    k = int(W, 17)

    if k == 1:
        print(int(N1)+int(N2))
    elif k == 2:
        print(int(N1)-int(N2))
    elif k == 3:
        print(int(N1)*int(N2))
    elif k == 4:
        print(int(N1)/int(N2))
    elif k > 4:
        print("invalid he BSDK")
    a = input("would u like to do something else(y/n)")
    if a.lower() != "y":
        break
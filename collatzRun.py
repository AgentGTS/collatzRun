from time import sleep

print("Enter a number higher than 1 for Collatz Conjecture run:")

try:
    x = input()
    x = int(x)

    while x <= 1:
        print("Input a number higher than 1:")
        x = input()
        x = int(x)

    while x <= 1:
        sleep(0.5)
        print("========")
        print("Next is: " + str(x))
        print("========")
        sleep(0.5)
        z = x
        while z != 1:
            sleep(0.1)
            if (z % 2 == 0):
                z = (z / 2)
                print(int(z))
            else:
                z = (z * 3) + 1
                print(int(z))
        x = x + 1

except ValueError or TypeError:
    print("Input a NUMBER, please.")

except KeyboardInterrupt:
    print("Run Stopped.")
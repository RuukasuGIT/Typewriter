import time
string = input("String: ")
delay = float(input("Delay: "))


def typewriter(x, z):
    y = ""
    for i in x:
        y += i
        print("\r", y, end="")
        time.sleep(z)


typewriter(string, delay)

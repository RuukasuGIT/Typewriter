import time
string = "Lorem ipsum dolor sit amet consectetur adipisicing elit."
delay = 0.1


def typewriter(x, z):
    y = ""
    for i in x:
        y += i
        print("\r", y, end="")
        time.sleep(z)


typewriter(string, delay)

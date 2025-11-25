# Debugging —`` შეცდომების პოვნა (საბაზისო მიდგომა)

# try/except

try:
    print(1 / 0)
except:
    print("Error")

# valueError

try:
    print(1 / 0)
except ValueError:
    print("Error")

# TypeError

try:
    print(1 / 0)
except TypeError:
    print("Error")

# KeyError

try:
    print(1 / 0)
except KeyError:
    print("Error")

# IndexError

try:
    print(1 / 0)
except IndexError:
    print("Error")

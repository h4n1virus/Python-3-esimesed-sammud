# Sander Viirmaa
# 19.12.2018
# Ülesanne 07 - 02


def tervita(a, b="de"):
    a = a.capitalize
    if "de" in b:
        print("Guten Morgen, {}".format(a))
    elif "en" in b:
        print("Hello, {}".format(a))
    elif "et" in b:
        print("Tere Hommikust, {}".format(a))



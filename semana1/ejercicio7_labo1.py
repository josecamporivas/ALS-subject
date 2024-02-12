conversion = {
    "a": "2", "b": "2", "c": "2",
    "d": "3", "e": "3", "f": "3",
    "g": "4", "h": "4", "i": "4",
    "j": "5", "k": "5", "l": "5",
    "m": "6", "n": "6", "o": "6",
    "p": "7", "q": "7", "r": "7", "s": "7",
    "t": "8", "u": "8", "v": "8",
    "w": "9", "y": "9", "z": "9"
}


def parser(num):
    x = 0
    if num[0] == "+":
        x += 1
        print("+", end="")
    if num[0:2] == "00":
        x += 1
        print("+", end="")
        num = num[2::]
    for i in num:
        if i.isdigit():
            x += 1
            print(i, end="")
        if conversion.get(i.lower()):
            x += 1
            print(conversion[i.lower()], end="")
        if x != 0 and x % 3 == 0:
            x = 0
            print(" ", end="")
    print()


numbers = ["(988) 387001", "+34 (988) 387001", "900 ESI NFO", "0034 (988) 387001"]
for number in numbers:
    parser(number)

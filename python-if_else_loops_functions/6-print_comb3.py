#!/usr/bin/python3
for chiffre1 in range(0, 9):
    for chiffre2 in range(1, 10):
        if chiffre1 == 8 and chiffre2 == 9:
            print("{}" "{}".format(chiffre1, chiffre2))
        elif chiffre1 != chiffre2 and chiffre1 < chiffre2:
            print("{}" "{}".format(chiffre1, chiffre2), end=", ")

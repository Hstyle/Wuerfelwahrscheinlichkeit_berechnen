from random import choice
import matplotlib.pyplot as plt

zahlen = [1, 2, 3, 4, 5, 6]
labels = '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'

ergebnis2 = 0
ergebnis3 = 0
ergebnis4 = 0
ergebnis5 = 0
ergebnis6 = 0
ergebnis7 = 0
ergebnis8 = 0
ergebnis9 = 0
ergebnis10 = 0
ergebnis11 = 0
ergebnis12 = 0
iterationen = 0


for i in range(10000):
        wuerfel1 = choice(zahlen)
        wuerfel2 = choice(zahlen)
        ergebnis = wuerfel1 + wuerfel2

        if ergebnis == 2:
                ergebnis2 += 1
        if ergebnis == 3:
                ergebnis3 += 1
        if ergebnis == 4:
                ergebnis4 += 1
        if ergebnis == 5:
                ergebnis5 += 1
        if ergebnis == 6:
                ergebnis6 += 1
        if ergebnis == 7:
                ergebnis7 += 1
        if ergebnis == 8:
                ergebnis8 += 1
        if ergebnis == 9:
                ergebnis9 += 1
        if ergebnis == 10:
                ergebnis10 += 1
        if ergebnis == 11:
                ergebnis11 += 1
        if ergebnis == 12:
                ergebnis12 += 1

        iterationen += 1

sizes = [ergebnis2/iterationen,ergebnis3/iterationen,ergebnis4/iterationen,ergebnis5/iterationen,ergebnis6/iterationen,ergebnis7/iterationen,ergebnis8/iterationen,ergebnis9/iterationen,ergebnis10/iterationen,ergebnis11/iterationen,ergebnis12/iterationen]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')
plt.show()
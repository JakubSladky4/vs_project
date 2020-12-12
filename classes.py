# -*- coding: utf-8 -*-
"""
Soubor definuje hlavní třídu trojuhelník, ze
které nadále vychází celý program. Rvněž definuje
funckci vstup(), která zpracovává vstup uživatele.

Created on Sat Dec 12 13:11:15 2020

@author: jakub
"""
import math


"""
Začátek definování tříd
"""


class trojuhelnik:

    Ax = 0
    Bx = 0
    By = 0
    Cx = 0
    Cy = 0

    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        """
        Konstruktor ke třídě trojuhelník.
        """
        self.Ax = float(Ax)
        self.Ay = float(Ay)
        self.Bx = float(Bx)
        self.By = float(By)
        self.Cx = float(Cx)
        self.Cy = float(Cy)

    def delkaStrany(self, strana):
        """
        Metoda, která vypočítá délku strany. Vstupním argumentem
        se určuje, která strana má být dopočítána.

        Args:
        Vstupem je argument string "strana", které má označovat, kterou stranu
        má funkce vrátit. Je možné tedy vkládat "a", "b" či "c". Dále
        funkce vychází z polí třídy trojuhelnik.
        """
        if strana == "a":
            x = math.pow((self.Bx - self.Cx), 2)
            y = math.pow((self.By - self.Cy), 2)
            return math.sqrt(x + y)
        elif strana == "b":
            x = math.pow((self.Ax - self.Cx), 2)
            y = math.pow((self.Ay - self.Cy), 2)
            return math.sqrt(x + y)
        elif strana == "c":
            x = math.pow((self.Bx - self.Ax), 2)
            y = math.pow((self.By - self.Ay), 2)
            return math.sqrt(x + y)
        else:
            return "Existují pouze strany a, b, c"

    def obvod(self):
        """
        Metoda, která vypočítá obvod trojuhelníku jakou součet jeho stran.

        Args:
        Žádné argumenty, metoda však používá k výpočtu pole třídy a
        metodu třídy obvod().
        """
        x = self.delkaStrany("a")
        y = self.delkaStrany("b")
        z = self.delkaStrany("c")
        return x + y + z

    def obsah(self):
        """
        Metoda, která vypočítá obsahu trojuhelníku
        dle Heronova vzorce.

        Args:
        Žádné argumenty, metoda však používá k výpočtu metody třídy
        obvod() a delkaStrany().
        """
        w = self.obvod()/2
        x = self.obvod()/2 - self.delkaStrany("a")
        y = self.obvod()/2 - self.delkaStrany("b")
        z = self.obvod()/2 - self.delkaStrany("c")
        return math.sqrt(w * x * y * z)

    def jeSestrojitelny(self):
        """
        Metoda, která určí zda je trojuhelník sestrojitelný či nikoliv.
        K určení využívá vlastnosti trojuhelníku, kdy pro každý trojuhelník
        platí, že součet jakýchkoliv dvou stran
        musí být větší než strana třetí.

        Args:
        Žádné argumenty, metoda však používá k výpočtu metodu třídy
        delkaStrany().
        """
        a = self.delkaStrany("a")
        b = self.delkaStrany("b")
        c = self.delkaStrany("c")
        if ((b + c) > a) and ((a + c) > b) and ((a + b) > c):
            return "ANO"
        else:
            return "NE"

    def jePravouhly(self):
        """
        Metoda, která určuje zda je trojuhelník pravoúhlý či nikoliv.
        K určení vychází z faktu, že pro pravoúhlé trojúhelníky platí
        Pythagorova věta. To znamená, že pro jednu ze stran musá platit, že
        její druhá mocnina je rovna součtu druhých mocnin zbývajících dvou
        stran.

        Args:
        Žádné argumenty, metoda však používá k výpočtu metody třídy
        obvod() a delkaStrany().
        """
        a = self.delkaStrany("a")
        b = self.delkaStrany("b")
        c = self.delkaStrany("c")
        if math.pow(a, 2) == math.pow(b, 2) + math.pow(c, 2):
            return "ANO"
        elif math.pow(b, 2) == math.pow(a, 2) + math.pow(c, 2):
            return "ANO"
        elif math.pow(c, 2) == math.pow(b, 2) + math.pow(a, 2):
            return "ANO"
        else:
            return "NE"


"""
Konec definování tříd
"""

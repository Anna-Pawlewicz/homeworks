import random


class Karta:

    def __init__(self, kolor, figura):
        self.kolor = kolor
        self.figura = figura

    def wyswietl(self):
        print("Figura:", self.figura)
        print("Kolor:", self.kolor)


class TaliaKart:

    def __init__(self, liczba_kart=52, kolory=4):
        self.liczba_kart = liczba_kart  # inicjalna liczba kart w talii
        self.kolory = kolory            # inicjalna liczba kolorów w talii
        self.karty = []                 # lista przechowująca wszystkie karty z talii
        self.utworz_karty()

    def utworz_karty(self):
        """Tworzy kombinację kart i uzupełniająca listę w talii"""
        kolory = ["Kier", "Karo", "Trefl", "Pik"]
        figury = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for kolor in kolory:
            for fig in figury:
                karta = Karta(kolor, fig)
                self.karty.append(karta)

    def przelicz(self):
        """Zwraca liczbę kart pozostałych w talii"""
        return len(self.karty)

    def tasuj(self):
        """Ta metoda ma w sposób losowy zmienić kolejność kart w talii
        (o ile w talii pozostały jakieś karty), a następnie zwrócić tę listę"""
        if len(self.karty) > 0:
            random.shuffle(self.karty)
            return self.karty

    def rozdaj(self):
        """Ta metoda ma zwrócić jedną kartę z talii i usunąć z listy"""
        wydana_karta = self.karty.pop()
        return wydana_karta

    def wyswietl_talie(self):
        """Ta metoda ma wyświetlić wszystkie karty w talii"""
        for karta in self.karty:
            karta.wyswietl()
        return


talia = TaliaKart()


#W miarę pisania kodu te poniższe asercje nie powinny rzucać błędami
assert talia.przelicz() == 52
talia.rozdaj()
assert talia.przelicz() == 51           # po jednym rozdaniu talia powinna zawierać jedną kartę mniej

#assert talia.karty != talia.tasuj()   Potasowanie talii powinny przestawić kolejność kart w liście
karty_nieprzetasowane = talia.karty.copy()
assert karty_nieprzetasowane != talia.tasuj()

for _ in range(talia.przelicz()):       # usuńmy wszystkie karty z talii i sprawdźmy, czy nic nie zostało
    talia.rozdaj()
assert talia.przelicz() == 0

try:
    talia.rozdaj()
except Exception as error:
    assert isinstance(error, IndexError)

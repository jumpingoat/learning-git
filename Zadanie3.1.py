#Zadanie 3.1
# zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
# Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: Idę do <sklep> i kupuję tam <rzeczy>.
# Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były wypisane wielką literą (sięgnij do oficjalnej dokumentacji, by odnaleźć taką funkcjonalność).
# Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.. X to sumaryczna liczba towarów, które są na listach.
# Twój program po uruchomieniu, powinien wyświetlić następujące informacje:

# Lista zakupów
# Idę do Piekarnia, kupuję tu następujące rzeczy: ['Chleb', 'Pączek', 'Bułki'].
# Idę do Warzywniak, kupuję tu następujące rzeczy: ['Marchew', 'Seler', 'Rukola'].
# W sumie kupuję 6 produktów.#


dict = {
    'piekarnia' : ['Chleb', 'Pączek', 'Bułki'],
    'warzywniak' : ['Marchew', 'Seler', 'Rukola']
}

liczba = 0
for sklep, zakupy in dict.items():
    print(f"Idę do {sklep.capitalize()} i kupuję tam {zakupy}")
    liczba += len(zakupy)
print(f"W sumie kupuję {liczba} rzeczy.")


# Zadanie 2
# Napisz program, który:
# - Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
# - W następnym wierszu wyświetli te liczby podniesione do potęgi 3.

number = [number for number in range(0, 101) if number % 5 == 0]
power = [number ** 3 for number in range(0, 101) if number % 5 == 0]
print(f"Liczby podzielne przez 5 to: {number}")
print(f"Te same liczby podniesione do 3 potęgi: {power}")


dict = {
    'piekarnia' : ['Chleb', 'Pączek', 'Bułki'],
    'warzywniak' : ['Marchew', 'Seler', 'Rukola']
}

liczba = 0
for sklep, zakupy in dict.items():
    print(f"Idę do {sklep.capitalize()} i kupuję tam {zakupy.capitalize()}")
    liczba += len(zakupy)
print(f"W sumie kupuję {liczba} rzeczy.")



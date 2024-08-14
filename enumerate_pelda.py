# Az ENUMERATE egy beépített Python függvény, amely nagyon hasznos lehet, amikor az indexet is szeretnéd tudni
# egy iteráció során. Segít abban, hogy egy iterálható objektum (például lista) minden eleméhez elérd az indexet is.
# Az ENUMERATE függvény egy összeísűrítés, amely két lista között történik, ezt a két listát akkr meg kell adni, illetve ha csak egy listánk van, akkor annak az indexét kapjuk meg, adja vissza. enumerate = összesűrítés
print(f"1. példa: ")
lista = ["alma", "banán", "cseresznye"]

for index, elem in enumerate(lista):
    print(f"Index: {index}, Elem: {elem}")

print(f"2. példa: ")

# Diákok nevei és pontszámai
diakok = ['Anna', 'Béla', 'Csaba', 'Dóra']
pontszamok = [85, 92, 78, 90]

# Az `enumerate` használata a diákok listáján
for index, diak in enumerate(diakok):
    # Index a sorszám, diak a diák neve
    pontszam = pontszamok[index]  # Az index segítségével elérjük a megfelelő pontszámot
    print(f"{index + 1}. {diak} pontszám: {pontszam}")

print("3. példa: ")

szoveg = "Python"

for index, karakter in enumerate(szoveg):
    print(f"Karakter: {karakter}, Index: {index}")
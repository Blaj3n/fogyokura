# Az enumerate egy beépített Python függvény, amely nagyon hasznos lehet, amikor az indexet is szeretnéd tudni
# egy iteráció során. Segít abban, hogy egy iterálható objektum (például lista) minden eleméhez elérd az indexet is.

lista = ["alma", "banán", "cseresznye"]

for index, elem in enumerate(lista):
    print(f"Index: {index}, Elem: {elem}")

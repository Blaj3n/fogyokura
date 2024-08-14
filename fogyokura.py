hetek_szama = int(input("Hetek száma="))
cel_testtomeg = float(input("Elérni kívánt testtömeg (kg)="))
tomegek = []
for het in range(1, hetek_szama+1):
    tomeg = float(int(input(f"{het}. héten=")))
    tomegek.append(tomeg)

cel_elert = False
index = 1

for tomeg in tomegek:
    if tomeg <= cel_testtomeg:
        print(f"Mari néni a(z) {index} héten érte el a célt.")
        cel_elert = True
        break
    index += 1

if not cel_elert:
    print("Sajnos Mari néni nem érte el a célját.")
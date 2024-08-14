hetek_szama = int(input("Hetek száma="))
cel_testtomeg = float(input("Elérni kívánt testtömeg (kg)="))
tomegek = []
for het in range(1, hetek_szama+1):
    tomeg = float(int(input(f"{het}. héten=")))
    tomegek.append(tomeg)

cel_elert = False
index = 1
nov_suly = 0
for tomeg in tomegek:
    if tomeg <= cel_testtomeg:
        print(f"Mari néni a(z) {index} héten érte el a célt.")
        cel_elert = True
        break
    index += 1
    if tomeg > cel_testtomeg:
        nov_suly += 1
print(f"A tömege {nov_suly} esetben nőtt egyik hétről a másikra. ")

if not cel_elert:
    print("Sajnos Mari néni nem érte el a célját.")


from sahkoauto import Sahkoauto
from polttomoottoriauto import Polttomoottoriauto

bensa = Polttomoottoriauto("ABC-25", 100, 50)
bensa.kiihtyvyys(40)
bensa.matka_tunti(3)
print(f"Bensa auto on kulkenut {bensa.kokonaismatka} KM")

sahko = Sahkoauto("ABC-15", 100, 50)
sahko.kiihtyvyys(50)
sahko.matka_tunti(3)
print(f"Sähko auto on kulkenut {sahko.kokonaismatka} KM")
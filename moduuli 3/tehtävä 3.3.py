Sukupuoli = str(input("Anna biologinen sukupuolisi: "))
Hemog = int(input("ja anna hemoglobiinin arvo g/l : "))

#Nainen
if Sukupuoli == "nainen" and Hemog < 117:
    print("Hemoglobiini on alhainen.")
elif Sukupuoli == "nainen" and Hemog > 175:
       print("Hemoglobiini on korkea.")
elif Sukupuoli == "nainen" and Hemog in range(117, 176):
    print("Hemoglobiini on nomaali.")

#Mies
if Sukupuoli == "mies" and Hemog < 134:
    print("Hemoglobiini on alhainen.")
elif Sukupuoli == "mies" and Hemog > 195:
    print("Hemoglobiini on korkea.")
elif Sukupuoli == "mies" and Hemog in range(134, 196):
    print("Hemoglobiini on nomaali.")

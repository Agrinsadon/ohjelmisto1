import math
#Ympyrä säteen pinta-ala laskelma

r_string = float(input("Anna ympyrän säde (m): "))
area = math.pi * r_string * r_string
print(f"{r_string} (m) säteisen ympyrän pinta-ala on n. {area:.3f} neliömetriä.")
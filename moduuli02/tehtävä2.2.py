import math
#Ympyrä säteen pinta-ala laskelma

r_string = input("Anna ympyrän säde (m): ")
r = float(r_string)
area = math.pi * r * r
print(f"{r} (m) säteisen ympyrän pinta-ala on n. {area:.3f} neliömetriä.")
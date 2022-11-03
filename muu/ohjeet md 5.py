

def tervehdi():
    print("Moro muhis!")
    print("Hyvää päivää!")
tervehdi()


#name on lokaali muuttuja (arvo ei näy funktion ulkouolelle
def say_hello(name):
    print(f"Moro {name}!")
    print("Hyvää päivää!")


# alla globaali name.muuttuja
name = "Churro"
say_hello("lines")
say_hello("Minni Hiiri")
print(name)


def sum_of_two_ints(number1, number2):
    results = number1 + number2
    print(f"{number1} + {number2} = {results}")
    return results #paluuarvo

              #tai

#def sum_of_two_ints(number1, number2):
    #results = number1 + number2
    #return results #paluuarvo

              # =

# funktiokutsu
results_sum = sum_of_two_ints(1, 2)
#print("Summa ",results_sum)
print("4 + 5=", sum_of_two_ints(4, 5))


# lottokone arpoo n numeroa 1-total numbers
import random
def create_lottery_row(number_amount, total_numbers):
    row = []
    for i in range(number_amount):
         rndNum = random.randint(1, total_numbers)
         while row.count(rndNum) > 0:
             #print("tuli tupla:", rndNum)
             rndNum = random.randint(1, total_numbers)
         row.append(rndNum)
         print(f"{i+1}. nro: {rndNum}")
    row.sort()
    return row

myrow = create_lottery_row(7, 39)
print("Lottorivi: ",myrow)


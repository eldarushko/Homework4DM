#6
from random import *

try:
    nimekirja = []
    N = int(input("Sisesta numbrite pikkus: "))
    for i in range(N):
        arv = randint(10, 100)
        nimekirja.append(arv)
    maksimum = max(nimekirja)  
    for i in range(len(nimekirja)):
        if nimekirja[i] == maksimum:
            nimekirja[i] = "useless_number"  
    print("Esialgne nimekiri: " + str(nimekirja))   
except ValueError:
    print("Palun sisesta korrektne arv")

#7
from random import *

try:
    sort_order = input("Kas soovite sorteerida kahanevas (k) või kasvavas (v) järjekorras?").lower()
    if sort_order not in ['k', 'v']:
        raise ValueError("Vale sisend. Sisesta 'k' või 'v'.")
    numbers = sorted([randint(-100, 100) for _ in range(6)], key=abs, reverse=sort_order == "k")
    print("Sorteeritud nimekiri: ")
    print(*numbers, sep="\n")
except ValueError as e:
    print("Viga: ", e)

#8
lists = [
   ['крот', 'белка', 'выхухоль'],
   ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],
   ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
]
try:
    max_length = 0
    for sublist in lists:
        for string in sublist:
            if len(string) > max_length:
                max_length = len(string)
    for sublist in lists:
        for i in range(len(sublist)):
            sublist[i] = sublist[i].ljust(max_length, '_')
    for sublist in lists:
        print(sublist)
except Exception as e:
    print("Viga: ", e)

#9
try:
    name = input("Введите ваше имя: ")
    if not name.isalpha():
        raise ValueError("Имя должно содержать только буквы")
    print("Tere,", name.capitalize())
    total_letters = len(name)
    vowels = sum(1 for letter in name if letter.lower() in 'aeiouаеёиоуыэюя')
    consonants = total_letters - vowels
    print("Nimes olevate tähtede arv: ", total_letters)
    print("Täishäälikute arv: ", vowels)
    print("Kaashäälikute arv: ", consonants)
    print("Tähed nimes tähestiku järjekorras: ", *sorted(set(name.lower())))
except ValueError as e:
    print("Viga:", e)
except Exception as e:
    print("Viga: ", e)

#12
from random import *

try:
    numbers = [random.randint(1, 100) for i in range(10)]
    print("Esialgne nimekiri: ", numbers)
    min_number = min(numbers)
    max_number = max(numbers)
    min_index = numbers.index(min_number)
    max_index = numbers.index(max_number)
    numbers[min_index], numbers[max_index] = max_number, min_number
    print("Loend pärast miinimum- ja maksimumelementide asendamist: ", numbers)
except Exception as e:
    print("Viga: ", e)


#16
from random import *

try:
    vastused = ["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!"]
    print("Tere tulemast küsimuste ja vastuste mängu!")
    while True:
        kysimus = input("Küsi jah/ei küsimus (väljumiseks kirjuta 'exit'): ")
        if kysimus.lower() == "exit":
            print("Aitäh mängimast! Nägemist!")
            break
        elif kysimus.endswith("?"):
            vastus = random.choice(vastused)
            print("Vastus: ", vastus)
        else:
            print("See ei tundu olevat jah/ei küsimus. Palun küsi jah/ei küsimus")
except Exception as e:
    print("Viga: ", e)

#?
from os import replace
from random import *
from string import *
from time import sleep
from turtle import clear 
#1v for 
for i in range(100): #i=0...99
    sym=i*"#"

    print(replace(sym))
    sleep(random)

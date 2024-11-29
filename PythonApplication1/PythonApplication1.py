from datetime import *
from calendar import *
from random import *
from math import *
from xml.sax import default_parser_list

#ulesanne 1

print("\n--- ulesanne 1 ---\n")

from datetime import date
from calendar import monthrange

# Получаем количество дней в ноябре (2024)
paevadekogus = monthrange(2024, 11)[1]  # calendar modulist
print(paevadekogus)

# Получаем текущую дату
tana = date.today()  # объект типа date
tana_str = tana.strftime("%B %d, %Y")  # строковое представление даты

# Выводим приветствие с текущей датой
print(f"Tere! Täna on {tana_str}")

# Получаем день, месяц и год
d = tana.day
m = tana.month
y = tana.year

print(d)
print(m)
print(y)

# Количество дней в декабре 2024
detsP = monthrange(2024, 12)[1]  # 31

# Количество дней в ноябре 2024
novP = monthrange(2024, 11)[1]  # 30

# Расчет оставшихся дней до конца года
jaak = detsP + novP - d

# Выводим результат
print(f"aasta lõppuni on {jaak}")


#ulesanne 2
print("\n--- ulesanne 2 ---\n")

vastus1 = 3 + 8 / (4 - 2) * 4
vastus2 = 3 + 8 / 4 - 2 * 4
vastus3 = (3 + 8) / (4 - 2) * 4
print (vastus1, "\n", vastus2, "\n", vastus3) # "\n" - с новой строки (в столбик)

#ulesanne 3
print("\n--- ulesanne 3 ---\n")

try:                    # если ошибка
    r=float(input("siseta R:")) #float только цифры с запятыми и ровные
    sk=pi*r**2 # две звездочки - это степень
    lk=2*pi*r
    skv=(2*r)**2 #возведение в квадрат две звездочки
    lkv=2*r*4
    print(f"ringe pindala on {sk}\nRingi ümbermõõt on {lk}\nRuudu pindala on {skv}\nRuudu ümbermõõt on {lkv}") # \n пишем слитно с переменной тогда будет выводить ровно, если ставим F то потом испольщзуем фигурные скобки
except: #если что то пошло не так
    print("on vaja number!")

#VARIANT 2

r=int(random ()*100) #0.0.111.0
print(f"R={r}")
sk=pi*r**2 # две звездочки - это степень
lk=2*pi*r
skv=(2*r)**2 #возведение в квадрат две звездочки
lkv=2*r*4
print(f"ringe pindala on {sk}\nRingi ümbermõõt on {lk}\nRuudu pindala on {skv}\nRuudu ümbermõõt on {lkv}") # \n пишем слитно с переменной тогда будет выводить ровно, если ставим F то потом испольщзуем фигурные скобки


#ulesanne 4
print("\n--- ulesanne 4 ---\n")

d=2.5 # mundi diameter sm +
maa=6378 # maa radius km
maa*=100000 #radius sm + maa=maa*100000
Lmaa=2*pi*maa
kogus=int(Lmaa/d)
print(f"0n vaja {kogus} mündi.\nMeil on vaja {kogus*2} eur")



#ulesanne 5
print("\n--- ulesanne 5 ---\n")

a="kill-koll". capitalize() #капитализм 1 буква заглавная
b="killadi-koll". capitalize()
print(a*2, b, a*2, b, a*4)

#ulesanne 6
print("\n--- ulesanne 6 ---\n")

#создаю две переменные песня 1 и песня 2 затем присваиваю песне 1 и 2 верхний регистр
pesenka_1 = """Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?"""

pesenka_2 = """Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""

print(pesenka_1.upper())
print()
print(pesenka_2.upper())

#ulesanne 7
print("\n--- ulesanne 7 ---\n")

pikkus = float(input("введите длину прямоугольника: "))
laius = float(input("введите ширину: "))
perimeter = 2*(pikkus+laius)
ploshad = pikkus * laius
print(f"периметр прямоугольника: {perimeter}")
print(f"площадь прямоугольника: {ploshad}")

#ulesanne 8
print("\n--- ulesanne 8 ---\n")

toplivo = float(input("введите количество топлива (в литрах): "))
print(f"залито {toplivo} литров ")
kilometr = float(input("какое расстояние проехали (в километрах): "))
print(f" проехали {kilometr} километров ")
srednee = toplivo / kilometr * 100
print(f"средний расходи топлива на 100км: {srednee:.2f} литров. ") #2.f (кол-во символов после запятой)

#ulesanne 9
print("\n--- ulesanne 9 ---\n")

print("средняя скорость конькобежца 29.9км/ч сколько проедет за минуту?")
skorost = 29.9
vremja = 60
otvet = skorost / vremja
print(f"конькобежец преодолевает за минуту {otvet:.2f} километров") #округлил для ровного

#вариант 2
print("\n--- ulesanne 9 вариант2 ---\n")

while True:
    skorost = float(input("Введите скорость 29.9км/ч: "))
    if skorost == 29.9:
        break
    else:
        print("Ошибка! введи именно 29.9км/ч: ")
skorost = 29.9
vremja = 60
otvet = skorost / vremja
print(f"Конькобежец преодолевает {otvet:.4f} км за 1 минуту.")


#ulesanne 10
print("\n--- ulesanne 10 ---\n")
minuta = float(input("введи количество минут: "))
otvet1 =  int(minuta // 60) # двойной слеш ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ что бы результат был полным числом
otvet2 = int(minuta % 60)
print(f"{otvet1} час(ов) {otvet2} минут")

#vigade otsing


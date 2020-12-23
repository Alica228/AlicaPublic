import pymorphy2
# заранее определяем валюту, в которой будем проводить расчёт
morph = pymorphy2.MorphAnalyzer()
RUB = morph.parse('рубль')[0]

def Price(age):
    """
    Функция вывода цены для конкретного возраста, прайс задаётся вручную

    Input:
    age -- возраст человека

    Output:
    price -- цена для конкретного возраста

    Keyword arguments:
    age -- int 

    """
    return {age < 18        : 0,
            18 <= age < 25  : 990,
            25 <= age        : 1390
        }[True]

while True:
    try:
        # считываем количество билетов
        numberOfTickets = int(input("Введите количество билетов: "))
        break
    except ValueError:
        print("Требуется число!\n")

while True:
    try:
        # считываем возраст для каждого из билетов
        agesForAllTickets = [int(input(f"Введите возраст для билета #{i+1}: ")) for i in range(numberOfTickets)]
        break
    except ValueError:
        print("Требуется число!\n")

# считаем сумму ориентируясь на прайс, если количество билетов больше 3 -> делаем скидку 10%
summa = sum([Price(age) for age in agesForAllTickets])
if numberOfTickets > 3:
    summa *= 0.9

print(f"Итоговая сумма: {summa:.0f} {RUB.make_agree_with_number(summa).word}")
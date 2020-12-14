per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму: "))
deposit = [int(money * i / 100) for i in per_cent.values()]
print(f"deposit = {deposit }")
print(f"Максимальная сумма, которую вы можете заработать — {max(deposit)}")
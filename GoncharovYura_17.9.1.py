
# Функция получения ввода последовательности и сортировки на ходу
# Получает от пользователя последовательность чисел и переводит в сортированный список
# Вывод: отсортированный список
def get_input():
    array = []
    while array == []: # Ждём ввод
        temp = input("Введите последовательность чисел: ").split(' ') # Сюда записывается пользовательский ввод
        for a in temp:
            if a == '': # удаляем пустые строки из списка ввода
                continue
            try:
                x = int(a) # преобразовывает строку в число, если поймаем ошибку - ждём ввод снова
                array.append(x) # добавляем число в итоговый список
                idx = len(array)-1 # на ходу сортируем список вставками
                while idx > 0 and array[idx-1] > x:
                    array[idx] = array[idx-1]
                    idx -= 1
                array[idx] = x
            except ValueError: # при нахождении ошибки - даём пользователю сообщение и начинаем с начала
                print("Требуется ввести числа!")
                array = []
                break
    return array

def binary_search(array, element, left, right): 
    middle = (right+left) // 2 # находим середину
    if array[middle] == element: # если элемент в середине,
        return middle-1 # возвращаем индекс поменьше
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)

array = get_input()
print(f"Отсортированная последовательность: {array}")
while True:
    try:
        element = int(input("Введите число: "))
        break
    except ValueError:
        print("Требуется ввести число!")

idx = binary_search(array, element, 0, len(array))
print(f"\nНомер позиции элемента: {idx},")
print(f"Который меньше введенного числа: {element},")
print(f"А следующий за ним больше или равен этому числу: {array[idx+2]},")
print(f"Значение этого элемента {array[idx]}.")
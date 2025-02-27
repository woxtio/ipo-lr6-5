# Написать программу, которая:
# - Создаёт с помощью генератора списков, список случайных целых чисел от **-50** до **50** размером **25** элементов.
# - Находит количество положительных, отрицательных и нулевых элементов в списке.
# - Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
# - Выводит самое большое и самое маленькое значение
import random  #Импортируем модуль random для генерации случайных чисел
spisok = [random.randint(-50, 50) for i in range(25)] #Создаем список из 25 случайных целых чисел в диапазоне от -50 до 50
pos = 0 #Счетчик для положительных значений
neg = 0 #Счетчик для отрицательных значений
zero = 0 #Счетчик для нулевых значений
for number in spisok: #Проходим по каждому числу в списке и подсчитываем количество положительных, отрицательных и нулевых чисел
    if number > 0:  # Есличисло положительное
        pos += 1  #Увеличиваем счетчик положительных чисел
    elif number < 0:  #Если число отрицательное
        neg += 1  #Увеличиваем счетчик отрицательных чисел
    else:  #Если число равно нулю
        zero += 1  #Увеличиваем счетчик нулевых чисел
vse_chisla = len(spisok) #Общее количество элементов в списке
pos_procent = (pos / vse_chisla) * 100 #Вычисляем процент положительных чисел
neg_procent = (neg / vse_chisla) * 100 #Вычисляем процент отрицательных чисел
zero_procent = (zero / vse_chisla) * 100 #Вычисляем процент нулевых чисел
min_element = min(spisok) #Находим минимальное значение в списке
max_element = max(spisok) #Находим максимальное значение в списке
print("Сгенерированный список: ", spisok) #Выводим сгенерированный список на экран
print("Количество положительных элементов: ", pos, pos_procent,"%") #Выводим количество положительных элементов и их процент
print("Количество отрицательных элементов: ", neg, neg_procent,"%") #Выводим количество отрицательных элементов и их процент
print("Количество нулевых элементов: ", zero, zero_procent,"%") #Выводим количество нулевых элементов и их процент
print("Самое большое значение: ", max_element) #Выводим самое большое значение в списке
print("Самое маленькое значение: ", min_element) #Выводим самое маленькое значение в списке

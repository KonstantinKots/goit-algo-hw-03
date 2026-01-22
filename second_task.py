import random
'''
Функція для генерації набору унікальних випадкових чисел

'''
num_min = int(input("Введіть найменьше число діапазону:"))
num_max = int(input("Введіть найбільше число діапазону:"))
quant = int(input("Введіть кількість чисел, які потрібно вибрати:"))

def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list:
    #створення списку унікальних випадкових чисел
    try:
        if num_min >=1 and num_max <=1000 and num_min < quant < num_max:
            num_list = random.sample(range(min_number, max_number), quantity)
            num_list.sort()
            return num_list
    except ValueError:
        if num_min < 1 and num_max <=1000 and num_min < quant < num_max
        print(f"Число {num_min} менше 1, введіть корректне число")


lottery_numbers = get_numbers_ticket(num_min, num_max, quant)
print("Ваші лотерейні числа:", lottery_numbers)

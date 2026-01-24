import random

def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> int:
    '''Функція для генерації набору унікальних випадкових чисел у заданому диапазоні

    :param date: Мінімальне та максимальне число діапазону, число вибірки у межах діапазону
    :type date: int
    :return: список з випадкових унікальних чисел
    :rtype: list

    '''
    #первірка вхідних данних
    if min_number < 1:
        print(f"Число {min_number} менше 1, введіть число >= 1.")
    elif max_number > 1000:
        print(f"Число {max_number} більше допустимого, введіть число менше 1000.")
    elif min_number > quantity or quantity > max_number:
        print(f"Число {quantity} не в межах чисел {min_number} та {max_number}.\
              \n Введіть корректне число.")

    #створення списку унікальних випадкових чисел
    try:
        if min_number >=1 and max_number <=1000 and quantity < max_number:
            num_list = random.sample(range(min_number, max_number+1), quantity)
            num_list.sort()
            return num_list
    except ValueError:
        return None

if __name__ == "__main__":
    min_num = int(input("Введіть найменьше число діапазону:"))
    max_num = int(input("Введіть найбільше число діапазону:"))
    quant = int(input("Введіть кількість чисел, які потрібно вибрати:"))
    lottery_numbers = get_numbers_ticket(min_num, max_num, quant)
    print("Ваші лотерейні числа:", lottery_numbers)

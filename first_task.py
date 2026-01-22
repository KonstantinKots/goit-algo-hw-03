
from datetime import datetime

date_str = input("Enter the date (year.month.day): ")     
today = datetime.now().date()                               

def get_days_from_today(date: str) -> int:
    '''
    Функція розраховує цілу кількість днів між сьогодняшньою та заданою датами
    
    :param date: рядок з датою в форматі YYYY.MM.DD
    :type date: str
    :return: різницю в днях або None якщо невірний формат дати
    :rtype: int
    '''
    
    try:
        #перетворюємо рядок у об'єкт date
        convert_date = datetime.strptime(date, '%Y.%m.%d').date()
        delta_days = today - convert_date
        return delta_days.days                                  
    except ValueError:
        #обробка невірного формату
        print("Enter, please, the date in the format: YYYY.MM.DD")
        return None
#викликаємо функцію    
result = get_days_from_today(date_str)
print(result)
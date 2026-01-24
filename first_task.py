
from datetime import datetime

def get_days_from_today(date: str) -> int:
    '''
    Функція розраховує цілу кількість днів між сьогодняшньою та заданою датами
    
    :param date: рядок з датою в форматі YYYY-MM-DD
    :type date: str
    :return: різницю в днях або None якщо невірний формат дати
    :rtype: int
    '''
    try:
        today = datetime.now().date()
        #перетворюємо рядок у об'єкт date
        convert_date = datetime.strptime(date, '%Y-%m-%d').date()
        delta_days = today - convert_date
        return delta_days.days
    except ValueError:
        #обробка невірного формату
        print("Введіть, будь ласка, дату у форматі: YYYY-MM-DD")
        return None

if __name__ == "__main__":
    date_str = input("Введіть дату (year-month-day): ")
    result = get_days_from_today(date_str)
    
    print(f"Різниця між датами складає: {result}")

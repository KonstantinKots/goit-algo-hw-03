
from datetime import datetime                 

date_str = input("Enter the date (year.month.day): ")     #введення данних користувачем
today = datetime.now().date                               #отримуємо сьогодняшню дату без часу

def get_days_from_today(date):                            #створюємо функцію для розрахунку різниці між датами
    try:
        convert_date = datetime.strptime(date, '%Y.%m.%d').date() #перетворюємо сторку у обєкт datetime
        delta_days = today() - convert_date                       #розраховуємо різницю між датами
        return delta_days.days                                    #повертаємо результат різниці між датами
    except:
        print("Enter, please, the date in the format: YYYY.MM.DD")  #обробка невірного введення формата дати
        

result = get_days_from_today(date_str)   #викликаємо функцію
print(result)                            
    


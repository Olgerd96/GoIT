from datetime import date, datetime, timedelta

print(f"Сегодня {date.today()}")
my_string = str(input('Enter date(yyyy-mm-dd): '))
my_date = datetime.strptime(my_string, "%Y-%m-%d")
#print(type(my_date), my_date)
next_date=my_date + timedelta(days=180)
print(f"Следующее чиппирование: {next_date}.")

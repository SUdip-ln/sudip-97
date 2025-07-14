from datetime import datetime

def days_between_dates(date1_str, date2_str):
    date_format = "%Y-%m-%d" 
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)


    delta = abs((date2 - date1).days)
    return delta

date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

days = days_between_dates(date1, date2)
print(f"Number of days between {date1} and {date2} is: {days}")



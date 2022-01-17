import datetime
import re

year_month = { 
  "january":0,
  "february":1,
  "march":2,
  "april":3,
  "may":4,
  "june":5,
  "july":6,
  "august":7,
  "september":8,
  "october":9,
  "november":10,
  "december":11

}

def calculate_years(year,month,day):
  today = datetime.date.today()
  user_date = datetime.date(year,month,day)
  passed_years = today - user_date

  return f"it is been {int(passed_years.days / 365)} years old!!!!"


get_date = input("Enter a valid date like this ('1970 january 1')\n-> ")


year_and_day = re.findall(r"[0-9]+", get_date)
month = re.search(r"[a-zA-Z]+", get_date)

year = int(year_and_day[0])
month = year_month[month.group()]
day = int(year_and_day[1])


print(calculate_years(year,month,day))

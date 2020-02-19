import datetime
from datetime import datetime
from datetime import timedelta
date_entry = input("Please enter LMP date in Format(dd-mm-yyyy):")
day, month, year = map(int, date_entry.split("-"))
LMP = datetime(year, month, day)
print("The LMP is", LMP.strftime("%d/%m/%Y"))

EDD = LMP + timedelta(days=280)
print("The EDD is", EDD.strftime("%d/%m/%Y"))

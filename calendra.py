'''import calendar
year=int(input("Enter year\t:"))
cal=calendar.TextCalendar(calendar.SUNDAY)
for i in range(12):
    print(end="")
    cal.prmonth(year,i+1)'''
import calendar
year=int(input("Enter Year\t:"))
cal=calendar.TextCalendar(calendar.SUNDAY)
for i in range(12):
    cal.prmonth(year,i+1)
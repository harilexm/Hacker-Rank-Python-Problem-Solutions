# Solution : 1
import calendar

def theday(month, day, year):
    weekday = calendar.weekday(year, month, day)
    today = calendar.day_name[weekday].upper()
    return today

m, d, y = list(map(int, input().split()))   
result = theday(m, d, y)
print (result)

# Solution: 2
import calendar

m, d, y = list(map(int, input().split()))

weekday = calendar.weekday(y, m, d)
today = calendar.day_name[weekday].upper()
print (today)

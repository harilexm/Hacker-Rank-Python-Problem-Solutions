# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

def theday(month, day, year):
    weekday = calendar.weekday(year, month, day)
    today = calendar.day_name[weekday].upper()
    return today



m, d, y = list(map(int, input().split()))   
result = theday(m, d, y)
print (result)

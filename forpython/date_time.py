# import datetime
# print(dir(datetime))##what are the funvions in the module


from datetime import datetime
now =datetime.now()
#or
# now =datetime(2024,10,1)
day =now.day
month=now.month
year=now.year
hr=now.hour
mn=now.minute
sec=now.second
#print(day,month,year,hr,mn,sec)
print(f'Day= {day} month={month} year={year} hour={hr} minute={mn} second={sec}')

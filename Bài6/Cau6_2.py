import datetime as dt
format ='%Y-%m-%dT%H:%M:%S'
tl=dt.datetime.strptime ("2008-10-12T14:45:52", format)
print('ngay  '+  str(tl.day))
print('thang ' + str(tl.month))
print('phut ' + str(tl.minute))
print('giay ' + str(tl.second))
# determine today's date and time
t2 = dt.datetime.now()
diff =  t2 - tl
print('chenh lech'+ str(diff.days), 'ngay')


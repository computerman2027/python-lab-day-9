import calendar
yy=int(input('Enter a Year: '))
for month in range (1,13):
    #it retrieves a list of weeks that represent the month
    mycal=calendar.monthcalendar(yy,month)
    week1=mycal[0]
    week2=mycal[1]
    if week1[calendar.MONDAY]!=0:
        auditday=week1[calendar.MONDAY]
    else:
        auditday=week2[calendar.MONDAY]
    print((calendar.month_name[month],auditday))
    print(mycal)
    print(calendar.TUESDAY)

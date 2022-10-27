from datetime import datetime

def agecal(years, months, days,year,month,date):
    import datetime
    td = datetime.date(years,months,days)
    d = datetime.date(year, month, date)
    years = ((td-d).total_seconds()/ (365.242*24*3600))
    yearsInt=int(years)
    months=(years-yearsInt)*12
    monthsInt=int(months)
    days=(months-monthsInt)*(365.242/12)
    daysInt=int(days)
    print("Present date =",td)
    print('Bilal, you are {0}, months {1}, days {2}.'.format(yearsInt,monthsInt,daysInt))


birthdate = input("Enter your birthdate(d/m/y) :")
my_date = datetime.strptime(birthdate, "%d/%m/%Y")
b_year = my_date.year
b_month = my_date.month
b_date = my_date.day
now = datetime.now()
c_year = int(now.strftime("%Y"))
c_month = int(now.strftime ("%m"))
c_date =int( now. strftime("%d"))
agecal(c_year,c_month, c_date, b_year, b_month, b_date)
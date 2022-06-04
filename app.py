import pywebio
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table

hour = 8760
day = 365
week = 56
month = 12
year = 1
principal = float(input("Starting balance (in $): "))
def interv_menu():
    print("Compounding Intervals")
    print("[H] Hourly")
    print("[D] Daily")
    print("[W] Weekly")
    print("[M] Monthly")
    print("[Y] Yearly")

interv_menu()
comp_interv = input("Enter compounding intervals: ")
print("Compounding frequency")
if comp_interv == "H":
    comp_fn = hour
    hourin = input("Compound every X Hours: ")
    compfn = hourin
    n = float(comp_fn) / float(compfn)
    if int(hourin) == 1:
        interval = "hour"
    elif int(hourin) >= 2:
        interval = "hours"
elif comp_interv == "D":
    comp_fn = day
    dayin = input("Compound every X Days: ")
    compfn = dayin
    n = float(comp_fn) / float(compfn)
    if int(dayin) == 1:
        interval = "day"
    elif int(dayin) >= 2:
        interval = "days"
elif comp_interv == "W":
    comp_fn = week
    weekin = input("Compound every X Weeks: ")
    compfn = weekin
    n = float(comp_fn) / float(compfn)
    if int(weekin) == 1:
        interval = "week"
    elif int(weekin) >= 2:
        interval = "weeks"
elif comp_interv == "M":
    comp_fn = month
    monthin = input("Compound every X Months: ")
    compfn = monthin
    n = float(comp_fn) / float(compfn)
    if int(monthin) == 1:
        interval = "month"
    elif int(monthin) >= 2:
        interval = "months"
elif comp_interv == "Y":
    comp_fn = year
    yearin = input("Compound every X Years: ")
    compfn = yearin
    n = float(comp_fn) / float(compfn)
    if int(yearin) == 1:
        interval = "year"
    elif int(yearin) >= 2:
        interval = "years"
t = float(input("Duration of interest earning in YEARS: "))
tt = int(t)
apr = float(input("Enter annaual interest rate (%): "))
final = int(principal * (1 + float(apr / 100) / float(n)) ** (n * t))
final_no_comp = int(principal + (principal * (apr/100) * t))
net = final - final_no_comp
net_perc = float(net / final_no_comp * 100)
intprincipal = int(principal)
if t == 1:
    y_length = "year"
elif t >= 2:
    y_length = "years"

put_markdown(" # If " + str(intprincipal) + "$ " + "is deposited as principal, " + "and interest is compounded every " + str(compfn) + " " + str(interval) + ", " + "after " + str(tt) + " " + "years, at " + str(apr) + "% APR, " "your total balance would be: ")
put_markdown(str(final) + "$")
put_markdown("And without compounding, your total balance would be: " + str(final_no_comp) + "$")
put_markdown("Which means that compounding every " + str(compfn) + " " + interval + " for " + str(tt) + " " + y_length + " nets you an extra: ")
put_markdown(str(net) + ", " + "or " + str(net_perc) + "% percent ")
put_table([
    ["Sum", "Sum (No Compound)", "Net extra ($)", "Net extra (%)"],
    [final, final_no_comp, net, net_perc]
])

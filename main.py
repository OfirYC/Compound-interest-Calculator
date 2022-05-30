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
elif comp_interv == "D":
    comp_fn = day
    dayin = input("Compound every X Days: ")
    compfn = dayin
    n = float(comp_fn) / float(compfn)
elif comp_interv == "W":
    comp_fn = week
    weekin = input("Compound every X Weeks: ")
    compfn = weekin
    n = float(comp_fn) / float(compfn)
elif comp_interv == "M":
    comp_fn = month
    monthin = input("Compound every X Months: ")
    compfn = monthin
    n = float(comp_fn) / float(compfn)
elif comp_interv == "Y":
    comp_fn = year
    yearin = input("Compound every X Years: ")
    compfn = yearin
    n = float(comp_fn) / float(compfn)
t = float(input("Duration of interest earning in YEARS: "))
apr = float(input("Enter annaual interest rate (%): "))
final = principal  * (1 + float(apr / 100) / float(n)) ** (n * t)
print(final)

import csv
fp = open("employees.csv","r")
csv_reader = csv.reader(fp)
employess = list(csv_reader)
print(employess)

for emp in employess[1:]:
 print(emp[0],": ",emp[1])
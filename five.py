import csv
fp= open("users.csv","r")
csv_reader=csv.reader(fp)
users=list(csv_reader)
users=users[1:]
print(users)

male_users =[]
for user in users:
    if user[2] =="Male":
        male_users.append((user[0],user[1],user[2]))
print(len(male_users))

fp2 = open("Male.csv","w")
csv_writer = csv.writer(fp2)
csv_writer.writerow(["uid","uname","ugender"])
csv.writer.writerows(male_users[(),(),()])
import json
fp1 =open("user.json","r")
users=json.load(fp1)
print(type(users))
print(len(users))

# transform
male_users=[]
female_users=[]
for user in users:
    if user['gender']=="Male":
        male_users.append(user)
    elif user['gender']=="Female":
        female_users.append(user)
print(len(male_users))
print(len(female_users))

# load
fp2=open("male.json","w")
fp3=open("female.json","w")
json.dump(male_users,fp2)
json.dump(female_users,fp3)

print("Created CSV files: male.csv and female.csv")
fp1.close()
fp2.close()
fp3.close()

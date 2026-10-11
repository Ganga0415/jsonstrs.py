import json
emp_json_str='''
        [{"eid":101,"ename":"RG","avail":true},
         {"eid":102,"ename":"SG","avail":false},
         {"eid":103,"ename":"PG","avail":false},
         {"eid":104,"ename":"Modi","avail":true},
         {"eid":105,"ename":"Amith","avail":true}
        ]
        '''
emp_list=json.loads(emp_json_str)
print(emp_list)

import json

employees_list=[{'eid': 101, 'ename': 'RG', 'avail': True, 'loc': None}, {'eid': 102, 'ename': 'SG', 'avail': False}, {'eid': 103, 'ename': 'PG', 'avail': False}, {'eid': 104, 'ename': 'Modi', 'avail': True}, {'eid': 105, 'ename': 'Amith', 'avail': True}]

print(type(employees_list))

emp_json_str=json.dumps(employees_list)
print(type(emp_json_str))
print(emp_json_str)

import json 

fp1=open('employees.json','r')

employees_list=json.load(fp1)
print(len(employees_list))

for emp in employees_list:
    print(emp['ename'])

employees = [] #list
employee = ('Abhi', 23, 60000, True)
employees.append(employee)

employee = ('Supriya', 22, 55000, True)
employees.append(employee)

employee = ('Ram', 23, 60000, True)
employees.append(employee)

print('after add all employee:', employees)
# search employee
I=0
search = 'Ram'
index = -1
for emp in employees:
    if emp[0] == search:
        index = I
        break
    I += 1

if index == -1:
    print('Employee not found')
else:
    search_employee = employees[index]
    print(search_employee)
    salary = float(input('Salary:'))
    employee = (search_employee[0],search_employee[1],search_employee[2])
    employees[index] = employee
print('after search and update:', employees)

employee = ('Harsha', 50, 200.75,True)
employees.append(employee)
print('after add Harsha:', employees)
employees.pop()#delete the last employee
print('after delete Harsha:', employees)
#delete employee Surpiya by position
postion = 1
employees.pop(postion)#delete the last employee
print('after delete Supriya:', employees)
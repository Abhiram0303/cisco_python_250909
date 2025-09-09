import repo
#test create employee and read all
employee = (101,'Abhi', 23, 60000, True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created sucessfully')
print('After add:', repo.read_all_employee())

employee = (102,'Supriya', 22, 55000, True)
print(f'Employee {employee[1]} created sucessfully')
print('After add:', repo.read_all_employee())

employee = (103,'Ram', 23, 60000, True)
print(f'Employee {employee[1]} created sucessfully')
print('After add:', repo.read_all_employee())

#test read by id
employee = repo.read_by_id(103)
if employee == None:
    print('Employee not found')
else:
    print(employee)

#test update
employee = repo.read_by_id(103)
if employee == None:
    print('Employee not found')
else:
    id, name, age, salary, is_active = employee
    salary += 20000
    new_employee = ( id, name, age, salary, is_active)
    repo.update(103, new_employee)
    print('After update:', repo.real_all_employee())

#test delete
repo.delete_employee(102)
print('After delete:', repo.real_all_employee())

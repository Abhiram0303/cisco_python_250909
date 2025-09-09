#CURD(create, read all | read one, update, delete)
employees = []

def create_employee(employee):
    global employees
    employees.append(employee)

def real_all_employee():
    return employees

def read_by_id(id):#new_employee is update
    for employee in employees:
        if employee[0] == id:
            return employee
        return None
    
def update(id, new_employee):
    I = 0
    for employee in employees:
        if employee[0] == id:
            employees[I] = new_employee
            break
    I += 1

def delete_employee(id):
    index = -1
    I = 0
    for employee in employees:
        if employee[0] == id:
            break
        I += 1
    if index != -1:
        employees.pop(index)
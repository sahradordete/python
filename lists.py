employees = ['Sara', 'Tammy', 'Debbie', 'John', 'Carrie']
print(employees)
employees = employees + ['Jim']
print(employees)
employees.insert(1, "Dave")
print(employees)

# deleting items of the list

del employees[4]
print(employees)

employees.remove("Carrie")
print(employees)


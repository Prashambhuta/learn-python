import json
def add_employee(salaries_json,name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

# testing the code
salaries = '{"Alfred": 300, "Jane" : 400}'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Me"])
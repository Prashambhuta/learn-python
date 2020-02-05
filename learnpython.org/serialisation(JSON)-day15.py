import json
def add_employee(salaries_json,name, salary):
    # define add employee function as function of 3 var

    salaries = json.loads(salaries_json)
    # whatever entery comes into salaries load that into the dataframe salaries_json

    salaries[name] = salary
    #recall the salaries function as salaries[name input] = salary


    return json.dumps(salaries)
#return the function salaries which will match the name with given salary


# testing the code
salaries = '{"Alfred": 300, "Jane" : 400}'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Me"])

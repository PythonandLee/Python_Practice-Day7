# When create a function, can dicide a value you want to return to the function.

def build_person(first_name, last_name, age=''):
    
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

person1 = build_person('kim', 'jason', age=23)
print(person1)
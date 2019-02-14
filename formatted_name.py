# The default for empty value is 'False'. 
# Use 'if-else' to determine if it has a 'middle_name'.
def get_formatted_name(first_name, last_name, middle_name=''):
    
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:    
        full_name = first_name + ' ' + last_name    
    return full_name.title()

# Be aware of positions. In 'def', the 'middle_name' valuation is in the last,
# so when insert values for functions, 
# the order will be 'first_name-> last_name -> middle_name'
name = get_formatted_name('leon', 'hans', 'roland')
name2 = get_formatted_name('elisa', 'jason')
print(name)
print(name2)
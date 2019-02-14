# Use 'for' to pass every elemets in the list.

def greet_users(names):
    
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
users = ['john', 'ronan', 'boddy']
greet_users(users)
# Use '*' in def to make valuation to be a tuple.

def make_pizza(size, *toppings):
    
    print("\nMaking a " + str(size)+ "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(15, 'cheese')
make_pizza(12, 'mushrooms', 'seafood', 'pepper')        
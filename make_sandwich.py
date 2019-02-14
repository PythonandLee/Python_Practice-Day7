# Use '*' can change 'def' valuations into tuples 
# which means can add more than one elements.

def sandwich_ingredients(*ingredients):
    
    print("\nFollowing are the ingredients you want to add in sandwich:")
    for ingredient in ingredients:
        print("- " + ingredient)

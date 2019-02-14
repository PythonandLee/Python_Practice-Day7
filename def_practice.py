def sandwich_ingredients(*ingredients):
    
    print("\nFollowing are the ingredients you want to add in sandwich:")
    for ingredient in ingredients:
        print("- " + ingredient)
        
sandwich_ingredients('tuna', 'egg', 'cheese')
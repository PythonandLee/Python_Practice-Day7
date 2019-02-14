# Create a function to combine information together, and could recall the
# function by insert relative function's values.
def city_country(city, country):
     combine = city.title() + ", " + country.title()
     return combine

print("\nPlease tell some city-country you have learned.")
city_insert = input("Insert a city: ")
country_insert = input("Insert the country: ")

combine_insert = city_country(city_insert, country_insert)
print(combine_insert)

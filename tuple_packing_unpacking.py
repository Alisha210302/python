name = input("Enter your name: ")
age = int(input("Enter the age: "))
city = input("Enter your city: ")
country = input("Enter your country: ")

tup1 = (name,age,(city,country))
print(tup1)

name_un , age_un , (city_un , country_un )= tup1
print(name_un)
print(age_un)
print(city_un)
print(country_un)

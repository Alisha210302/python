import random
countries_and_capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'Portugal': 'Lisbon',
    'Netherlands': 'Amsterdam',
    'United Kingdom': 'London',
    'Canada': 'Ottawa',
    'Japan': 'Tokyo',
    'Australia': 'Canberra',
}

def quiz():
    countries = list(countries_and_capitals.keys())
    random.shuffle(countries)

    correct_ans = 0

    for country in countries:
        user_answer = input(f"Enter the capital of {country} starting with a capital letter:  ")

        if user_answer == countries_and_capitals[country]:
            print("Correct answer")
            correct_ans+=1
        else:
            print(f"incorrect answer{countries_and_capitals[country]}")

    print(f"You got {correct_ans} answers correct!")

quiz()





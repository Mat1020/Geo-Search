import time, random
from Data import nearby_countries

TOTAL_COUNTRIES = 21

countries = [
    "venezuela",
    "united states",
    "chile",
    "germany",
    "japan",
    "france",
    "italy",
    "united kingdom",
    "china",
    "south korea",
    "canada",
    "russia",
    "israel",
    "brazil",
    "india",
    "spain",
    "australia",
    "new zealand",
    "honduras",
    "north korea",
    "morocco"
]

options = {
    "capital": 1,
    "continent": 2,
    "area": 3,
    "population": 4,
    "highest point": 5,
    "neighboring countries": 6,
    "language(s)": 7,
    "fun fact": 8
}

def loop_options():
    print()
    for key, value in options.items():
        print(f"{key.title()}: {value}")
        time.sleep(0.5)

def venezuela(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.venezuela_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)
            elif user_input == "7":
                pass
            elif user_input == "8":
                pass
            else:
                print(f"Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid choice next time.")
            time.sleep(2)

def united_states(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.united_states_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def chile(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.chile_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def germany(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            quit()

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.germany_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def japan(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def france(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            quit()

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.france_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)

        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def italy(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.italy_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def united_kingdom(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.united_kingdom_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def china(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} B.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.china_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(3)
        else:
            print("Please type a valid option next time.")
            time.sleep(3)

def south_korea(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.china_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def canada(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.canada_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def russia(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.russia_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def israel(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            quit()

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.israel_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def india(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} B.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.india_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def brazil(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.brazil_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def australia(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        user_input = int(user_input)
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def new_zealand(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def spain(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.spain_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def honduras(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.honduras_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def north_korea(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.north_korea_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

def morocco(capital, continent, area, population, highest_point, neighboring_countries):
    while True:
        loop_options()
        print()
        user_input = input(f"What whould you like to know about {country.title()} or hit enter to quit: ")

        if user_input == "":
            break

        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                print(f"The capital of {country.title()} is {capital.title()}.")
                time.sleep(3)

            elif user_input == 2:
                print(f"The continent of {country.title()} is {continent.title()}.")
                time.sleep(3)

            elif user_input == 3:
                print(f"The area of {country.title()} is {area} mi.")
                time.sleep(3)

            elif user_input == 4:
                print(f"The population of {country.title()} is {population} M.")
                time.sleep(3)

            elif user_input == 5:
                print(f"The highest point of {country.title()} is {highest_point} ft.")
                time.sleep(3)

            elif user_input == 6:
                print(f"The neighboring countries of {country.title()} is {neighboring_countries}.")
                time.sleep(1.5)
                print("They are:")
                time.sleep(1)
                for x in nearby_countries.morocco_neighboring_countries:
                    print(f"  - {x.title()}")
                    time.sleep(0.5)
                time.sleep(3)

            else:
                print("Please check if you typed correctly next time.")
                time.sleep(2)
        else:
            print("Please type a valid option next time.")
            time.sleep(2)

for i, country in enumerate(countries, 1):
    print(i, country.title())
    time.sleep(0.3)

time.sleep(1.50)
while True:
    country = input("Type the Name/Number of the country you would like to know about or Q to quit: ")
    if country.lower() == "q":
        quit()

    elif country.lower() in countries:
        break

    elif country.isdigit():
        country = int(country)
        if 1 <= country <= TOTAL_COUNTRIES:
            break
        else:
            print(f"Country number must be bewteen: 1 - {TOTAL_COUNTRIES}")
    else:
        print("Please type a valid country NAME or NUMBER next time.")

if country == "venezuela" or country == 1:
    country = str("venezuela")
    venezuela("caracas", "south america", "353,841", 28.3, "16,342", 3)

elif country == "united states" or country == 2:
    country = str("united states")
    united_states("washington d.c", "north america", "3,677,648", 334.7, "20,321", 2)

elif country == "chile" or country == 3:
    country = str("chile")
    chile("santiago", "south america", "291,933", 20, "22,615", 3)

elif country == "germany" or country == 4:
    country = str("germany")
    germany("berlin", "europe", "137,988", 84.3, " 9,718", 9)

elif country == "japan" or country == 5:
    country = str("japan")
    japan("tokyo", "asia", "145,920", 124.5, "12,388", 0)

elif country == "france" or country == 6:
    country = str("france")
    france("paris", "europe", "247,367", 68, "15,781", 8)

elif country == "italy" or country == 7:
    country = str("italy")
    italy("rome", "europe", "116,346", 58.9, "15,781", 6)

elif country == "united kingdom" or country == 8:
    country = str("united kingdom")
    united_kingdom("london",  "europe", "93,628", 67, "4,409", 1)

elif country == "china" or country == 9:
    country = str("china")
    china("beijing", "asia", "3,705,406", 1.41, "29,029", 14)

elif country == "south korea" or country == 10:
    country = str("south korea")
    south_korea("seoul", "asia", "38,691", 51.4, "6,398", 1)

elif country == "canada" or country == 11:
    country = str("canada")
    canada("ottawa", "north america", "3,855,101", 39.9, "19,550", 1)

elif country == "russia" or country == 12:
    country = str("russia")
    russia("moscow", "europe & asia", "6,601,667", 146.4, "18,510", 14)

elif country == "israel" or country == 13:
    country = str("israel")
    israel("jerusalem", "asia", "8,019", 9.7, "3,963", 4)

elif country == "india" or country == 14:
    country = str("india")
    india("new delhi", "asia", "1,269,219", 1.39, "28,169", 8)

elif country == "brazil" or country == 15:
    country = str("brazil")
    brazil("brasilia", "south america", "3,287,955", 216.1, "9,823", 10)

elif country == "australia" or country == 16:
    country = str("australia")
    australia("canberra", "australia (oceania)", "2,969,906", 26.5, "9,006", 0)

elif country == "new zealand" or country == 17:
    country = str("new zealand")
    new_zealand("welington", "australia (oceania)", "104,428", 5.2, "12,316", 0)

elif country == "spain" or country == 18:
    country = str("spain")
    spain("madrid", "europe", "195,365", 47.6, "12,198", 5)

elif country == "honduras" or country == 19:
    country = str("honduras")
    honduras("tegucigalpa / comayaguela", "north america", "43,433", 9.5, "9,416", 3)

elif country == "north korea" or country == 20:
    country = str("north korea")
    north_korea("pyongyang", "asia", "46,541", 25.7, "9,003", 3)

elif country == "morocco" or country == 21:
    country = str("morocco")
    morocco("rabat", "africa", "172,414", 36.9, "13,671", 3)

quit()
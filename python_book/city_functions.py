
def city_country(city, country, population=None):
    """
    Takes a city name and country name and returns a formatted
    string denoting the city and country separated by a comma
    """
    output_no_pop = city.title() + ", " + country.title() 
    output_pop = city.title() + ", " + country.title() + " - "\
            "population " + str(population)

    if population:
        output = output_pop
    elif population is None:
        output = output_no_pop

    return output
#    print(city)
#    print(country)
#    print(output)


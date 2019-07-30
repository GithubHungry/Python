def city_country_name(city, country, population=''):
    """return nice name of city+country"""
    if population:
        nice_name = city.title() + ', ' + country.title() + ', population: ' + str(population)
    else:
        nice_name = city.title() + ', ' + country.title()
    return nice_name

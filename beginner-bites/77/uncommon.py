def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    return len(list(set(my_cities) - set(other_cities)) + list(set(other_cities) - set(my_cities)))

def rabbit_recursive(months, litter_size):
    adults = 0
    newborns = 1
    for month in range(months):
        adults, newborns = adults + newborns, adults * litter_size
    return adults

print(rabbit_recursive(33,3))
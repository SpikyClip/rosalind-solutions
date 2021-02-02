months = 6
lifespan = 3

# Initialises a list with positions for each possible 'age' for a given lifespan
# this list will store the rabbits
# list is lifespan + 1 long, as rabbits die in the month after their lifespan
rabbits = [month*0 for month in range(lifespan+1)]

#iterates through the months
for month in range(months):

#supplies the initial newborn rabbit for the first month
    if month == 0:
        monthly_births = 1

#in the second month, no rabbits are born as the first pair has only just matured
    elif month == 1:
        monthly_births = 0

#in the third month and beyond, breeding occurs. The monthly births are the sum
#of rabbits in the list excluding the newborns rabbits[-1] and the rabbits about
#to die rabbits[0]

    elif month > 1:
        monthly_births = sum(rabbits[1:-1])

    monthly_deaths = rabbits.pop(0)
    rabbits.append(monthly_births)

    message = f'''{(str(month+1)+ ' month').center(80, '-')}

Monthly Deaths: {monthly_deaths}
Monthly Births: {monthly_births}
Current Rabbits by Age (Oldest to Youngest): {rabbits[1:]}
Total Rabbits: {sum(rabbits[1:])}
'''
    print(message)

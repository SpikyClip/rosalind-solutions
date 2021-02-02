def mortalfib(months, lifespan):
    '''Returns the number of rabbits after x months given a lifespan of 
    y months. Rabbits can only become pregnant a month after they are 
    born, and pregnancies turn into births the following month.'''

    # Initialises a list that will contain the number of rabbits for 
    #each generation, from oldest (index 0) to youngest (index -1)
    rabbits = [month*0 for month in range(lifespan)]

    #iterates through the months, index beginning with 1 for clarity
    for month in range(1,months+1):

        if month == 1:
            # Supplies the initial newborn rabbit for the first month
            monthly_births = 1
            # No pregnancies occur, as rabbits haven't reached maturity.
            #Pregnancies set to zero, to supply 0 births in month 2
            monthly_pregnancies = 0

        elif month >= 2:
            # Pregnancies in the previous month become births
            monthly_births = monthly_pregnancies
            # Pregnancies this month are the sum of all rabbits in the 
            #list excluding those about to die (index 0). Index -1 is 
            #included here, as newborns have not been recorded into the 
            #list yet
            monthly_pregnancies = sum(rabbits[1:])

        # Records death and births into the rabbit list
        monthly_deaths = rabbits.pop(0)
        rabbits.append(monthly_births)

        # Monthly printout for troubleshooting
        message = f'''{(str(month)+ ' month').center(80, '-')}

        Monthly Deaths: {monthly_deaths}
        Monthly Births: {monthly_births}
        Monthly Pregnancies: {monthly_pregnancies}
        Current Rabbits by Age (Oldest to Youngest): {rabbits}

        Total Rabbits: {sum(rabbits)}
        '''
        print(message)

    return sum(rabbits)

print(mortalfib(87, 20))
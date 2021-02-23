# url: http://rosalind.info/problems/fibd/

# Problem

# Recall the definition of the Fibonacci numbers from “Rabbits and
# Recurrence Relations”, which followed the recurrence relation
# Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in
# one month and produces a single pair of offspring (one male, one female)
# each subsequent month.

# Our aim is to somehow modify this recurrence relation to achieve a dynamic
# programming solution in the case that all rabbits die out after a fixed
# number of months. See Figure 4 for a depiction of a rabbit tree in which
# rabbits live for three months (meaning that they reproduce only twice
# before dying).

# Given: Positive integers n≤100 and m≤20.

# Return: The total number of pairs of rabbits that will remain after the
# n-th month if all rabbits live for m months.


def mortal_rabbit_recursive(months, lifespan):
    """
    return total no. of rabbit pairs after n months given adult pairs
    produce 1 pair of newborns each month, and die after lifespan
    """
    # generates adult.pop() buffer given a specified lifespan
    adults = [0 for i in range(lifespan)]

    for month in range(1, months + 1):
        # supplies initial newborn
        if month < 2:
            newborns = 1
        else:
            # Newborns turn into adults and are appended, but the newborn
            # of this generation come from the adults of the previous
            # hence adults[:-1]
            adults.append(newborns)
            newborns = sum(adults[:-1])
        # the adult list is popped from the front every month. The
        # lifespan buffer of zeroes ensures deaths don't come into effect
        # until lifespan no. of months has elapsed
        adults.pop(0)

    return sum(adults) + newborns


if __name__ == "__main__":
    file1, file2 = "inputs/FIBD_input.txt", "outputs/FIBD_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        # test = map(int, f1.read().split())
        # print(test)
        months, lifespan = map(int, f1.read().split())
        f2.write(str(mortal_rabbit_recursive(months, lifespan)))
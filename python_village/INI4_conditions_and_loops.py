#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.

a = 4631
b = 9089
odd_integers = []
integers = list(range(a,b+1))
for number in integers:
    if number % 2 != 0:
        odd_integers.append(number)

print(sum(odd_integers))
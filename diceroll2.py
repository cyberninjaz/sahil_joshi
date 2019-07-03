import random
print("please put the times you want to roll the dice, the number of side on the dice, and how much you want to add")
times=int(input())
sides=int(input())
add = int(input())
final = 0
for i in range(times):
    final = final + random.randint(1,sides)

print(final+ add)

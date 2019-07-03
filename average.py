print("please type in how many numbers you want and I will find the average")
numbers = int(input())
total = 0
for i in range(numbers):
    total = total + float(input())

print(total/numbers)
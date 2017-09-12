i = 0
numbers = [] # use [] to make a list

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i) # add i to the list

    i = i + 1
    print("Numbers now:", numbers)
    print("At the bottom i is %d" % i) # print the current number

print("The numbers:")

for num in numbers:
    print(num) # print all numbers in the list

input = input()
summ = 0
for element in input.split(' '):
    summ += float(element)

print(summ / len(input.split(' ')))
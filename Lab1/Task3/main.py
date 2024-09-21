inputNumber = int(input("Введите число: "))
digitsSum = 0
while inputNumber > 0:
  digitsSum += inputNumber % 10
  inputNumber = inputNumber // 10

print(f'Сумма цифр числа: {digitsSum}')
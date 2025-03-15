from random import randrange

# - - Генерация случайных чисел - - #
def sum(n): 
   i = 0
   sum = 0
   numbers = list()
   for i in range(n):
      numbers.append(randrange(0, 255))
      if numbers[i] % 2 == 0:
         sum += numbers[i]
   print("Список случайных чисел:",  numbers)
   print("Сумма всех четных чисел в списке:", sum)
print(sum(10))




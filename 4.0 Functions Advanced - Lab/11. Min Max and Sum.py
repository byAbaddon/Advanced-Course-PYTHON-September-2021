def min_max_sum(numbers):
   numbers = [int(x) for x in numbers.split()] 
   min_num = min(numbers) 
   max_num = max(numbers)
   sum_min_max = sum(numbers)
   return f'The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_min_max}'


print(min_max_sum(input()))
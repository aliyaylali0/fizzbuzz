fizzbuzz_list = []
for number in range(1,101):
  fizzbuzz_list.append(number)
  if number % 3 == 0:
    fizzbuzz_list.pop()
    fizzbuzz_list.append("Fizz")
  if number % 5 == 0:
    fizzbuzz_list.pop()
    fizzbuzz_list.append("Buzz")
  if number % 3 == 0 and number % 5 == 0:
    fizzbuzz_list.pop()
    fizzbuzz_list.append("FizzBuzz")

for fizz in fizzbuzz_list:
  print(fizz)

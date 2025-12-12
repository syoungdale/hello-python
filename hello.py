import numpy as np

print("Hello, World!")

x = 5   # integer
y = 3.2 # float
name = "John" # string
is_ready = True # boolean

print(x, y, name, is_ready)

# Arithmetic Operators
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) # modulus
print(x ** y) # exponent

scores = [100, 90, 80, 70, 60]

print(scores[0]) # first element
print(scores[1]) # second element
print(scores[2]) # third element
print(scores[3]) # fourth element
print(scores[4]) # fifth element

print(scores[-1]) # last element
print(scores[-2]) # second last element
print(scores[-3]) # third last element
print(scores[-4]) # fourth last element
print(scores[-5]) # fifth last element  

print(scores[0:3]) # first three elements

scores.append(50) # add 50 to the end of the list
print(scores)   # [100, 90, 80, 70, 60, 50]

# Exercises

# 1. Create a list of the cubes of numbers 0-9
cubes = [i**3 for i in range(10)]
print(cubes)

# 2. Create a list of only the even numbers between 1 and 50.
evens = []
for number in range(1,51):
    if number % 2 == 0:
        evens.append(number)
print (evens)

# This does the same thing, but in a single line
evens_short = [n for n in range(1,51) if n % 2 == 0]
print(evens_short)

# 3. Convert a list of temperatures in Celsius to Fahrenheit.
temps_c = np.array([0, 10, 20, 30, 40])
print(temps_c)
temps_f = (temps_c * 9 / 5 + 32)
print(temps_f)

# 4. Extract all names that start with "A"
names = ["Alice", "Sam", "Alex", "Jordan", "Andrew", "Mike"]
A_names = [name for name in names if name.startswith("A")]
print(A_names)

# 5. Build a list of (number, square, cube) tuples for 1-10
# Result example: [(1, 1, 1), (2, 4, 8), ..., (10, 100, 1000)]
stacked_list = [(i, i**2, i**3) for i in range(1, 11)]
print(stacked_list)

# 6. Write a function that returns the sum of all numbers in a list.
list_to_sum = [1, 2, 3, 7, 9, 3]
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(sum_list(list_to_sum))

# 7. Write a function that counts how many even numbers are in a list
list_to_even = [1, 2, 3, 7, 9, 3, 4, 22]
def count_even(input_list):
    even_num = 0
    for n in input_list:
        even_num += 1 if n % 2 == 0 else 0
    return even_num

def count_even_python(input_list_python):
    return sum(1 for n in input_list_python if n % 2 == 0)

print(count_even(list_to_even))
print(count_even_python(list_to_even))

# 8. Write a function that returns the largest number in a list.
list_to_check = [1, 2, 3, 7, 9, 3, 4, 22]
def list_max(input_list):
    return max(input_list)

def list_max_hard(input_list):
    max_list = 0
    for n in input_list:
        max_list = n if n > max_list else max_list
    return max_list

print(list_max(list_to_check))
print(list_max_hard(list_to_check))

# 9. Write a loop that prints numbers from 10 down to 1.
#for i in range(1, 11):
#    print(11-i)

# 10. Write a function to compute factorial using a loop.

def factorial(number):
    output = 1
    for i in range(number, 1, -1):
        output = output * i
    return output

print("Factorial output is:",factorial(5))

# 11. Given this dictionary, print just the keys
person = {"name": "Sam", "role": "Engineer", "age": 30}
print(person)
for key in person:
    print(key)

print(list(person.keys()))

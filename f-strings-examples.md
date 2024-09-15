### Python: F-Strings

- **f-string** is short for **formatted string**
- f-strings were introduced in Python 3.6
- f-strings make it easy to embed variables and expressions in a string


### Using a Variable in an F-String
```python
# Inserting the value John in the f-string
first_name = 'John'
greeting = f'Hello, {first_name}!'
print(greeting)

# Output
Hello, John!
```

### An Expression in an F-String
Adding an expression to an f-string is possible, but the preferred
method is to have Python do the math, assign the answer to a variable,
and then print the value stored in the variable.

```python
# The expression is 2 + 3
result = f'{2 + 3}'
print(result)

# Output
5

# Assign the answer to a variable
num1 = 2
num2 = 3
answer = num1 + num2
output_string = f'The sum of {num1} and {num2} is: {answer}'
print(output_string)

# Output
The sum of 2 and 3 is: 5
```

### Multline F-Strings

Use a pair of triple quotes if you want to spread an
f-string over multiple lines.

```python
first_name = 'John'
website = 'YouTube.com'

message = f'''{first_name} is learning Python by
watching Python tutorials for beginners
on {website}.'''
print(message)

# Output
John is learning Python by
watching Python tutorials for beginners
on YouTube.com.
```

# Formatting Numbers in F-Strings

In an f-string, you can specify the number of decimal places you
want your number to have.
```python
# Number will display two places after the decimal point
# Number will also be rounded to 9.99
number = 9.98567
output_str = f'{number: .2f}'
print(output_str)

# Output
9.99


# If a number is very large, add commas to make it easier to read

large_number = 400000000000
formatted_number = f'{large_number: ,}'  
print(formatted_number)  

# Output
400,000,000,000


# Formatting a number as a percentage
my_number = 0.1259

# Show two places after the decimal point
two_places = f'{my_number: .2%}'
print(two_places)

# Output
12.59%

# Show one place after the decimal point
one_place = f'{my_number: .1%}'
print(one_place)

# Output
12.6%
```





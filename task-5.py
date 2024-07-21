
##task-05
data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))

##using lambda function
data = [1, "hello", 3.14, "world", 42, "Python", [1, 2, 3], 99]

check_type = lambda x: isinstance(x, (int, str))
result = list(map(check_type, data))

print(result)

##using lambda function create fibonacci series
from functools import reduce

fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])

# Generate Fibonacci series up to 50 elements
fib_series = fibonacci(50)

print(fib_series)

##using python regular expression -check email addres
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

email = "example@example.com"
print(validate_email(email))
#check mobile number of bangladesh
def validate_bd_mobile_number(number):
    pattern = r'^(\+88)?01[3-9]\d{8}$'
    return bool(re.match(pattern, number))

bd_mobile_number = "+8801712345678"
print(validate_bd_mobile_number(bd_mobile_number))

#telephone number of usa
def validate_usa_telephone_number(number):
    pattern = r'^(\+1)?[2-9]\d{2}[2-9](?!11)\d{6}$'
    return bool(re.match(pattern, number))

usa_telephone_number = "+12345678901"
print(validate_usa_telephone_number(usa_telephone_number))

#16 alpha - numeric password
def validate_password(password):
    pattern = r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{16}$'
    return bool(re.match(pattern, password))

password = "Aa1!Aa1!Aa1!Aa1!"
print(validate_password(password))
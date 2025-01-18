#definining the functions
# def sum(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def mul(a,b):
#     return a * b

# def div(a,b):
#     return a / b

# #variables
# pi = 3.14
# username = "admin"
# password = "admin123"

numbers = [8,2,3,0,7,1,4,8,9]

def my_sum (numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result= my_sum(numbers)
print("The sum is:", result)
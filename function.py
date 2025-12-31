#create a function to calculate the volume of cuboid

# def volume_of_cuboid(length,width,height):
    
#     return length*width*height

# vol=volume_of_cuboid(10,5,15)
# print(f"volume:{vol}")


#reverse the list using function call
#take list as argument and return a reversed list 

# def reverse_list_slicing(data):
#     """Takes a list and returns a new reversed list."""
#     return data[::-1]

# original_list = [1, 2, 3, 4, 5]
# new_list = reverse_list_slicing(original_list)

# print("Reversed:", new_list)      

#repeat same message multiple n time usinf function 

# def repeat_message(message, times):
#     for _ in range(times):
#         print(message)

# repeat_message("Hello!", 3)

#recursive functions
# fibonacci series

# def fibonacci(n):
#     if n <= 1 :
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    

# print(fibonacci(6))

#sum of natural number using recursive function 

# def sum_natural_number(n):
#     if n==1 :
#         return n 
#     else:
#         return n + sum_natural_number(n-1)

# print(sum_natural_number(5))

#from the list find the smallest number using the recursive function

# def find_smallest_recursive(numbers_list):
#     if len(numbers_list) == 1:
#         return numbers_list[0]
#     else:
#         sub_min = find_smallest_recursive(numbers_list[1:])
#         return numbers_list[0] if numbers_list[0] < sub_min else sub_min
    

#palindrome number 

#high order function


# def reverse_output(func):
#     def wrapper(*args, **kwargs):
        
#         result = func(*args, **kwargs)

#         if (result, str):
#             return result[::-1]
#         return result
#     return wrapper

# @reverse_output
# def get_text(name):
#     return f"Bashyal {name}"

# print(get_text("Anuj"))

# def multiplier(factor):
#     def multiply_by_factor(number):
#         return number * factor
#     return multiply_by_factor

# multiplier_value = multiplier(5)
# print(multiplier_value._name_)


# built in higher order function map, filter , reduce 

# def square(num):
#     return num ** 2

# numbers=[1,2,3,4,5]

# squared_numbers = map(square, numbers)

# print(list(squared_numbers))


# def divisible(num):
#     if num % 2 == 0:
#         return True
#     else :
#         return False
# numbers=[1,2,3,4,5]

# divisible_numbers = map (divisible, numbers)

# print(list(divisible_numbers))


# words = ['anuj', 'ronaldo', 'neymar']
# result = list(map(str.upper, words))
# print(result) 
    


#find the sum of each nested list and return true or fals if sum is greater than 10 using map function 

# nested_list = [[1, 2], [15, 5], [2, 1], [7, 4]]

# def is_sum_over_10(sublist):
#     return sum(sublist) > 10

# results = list(map(is_sum_over_10, nested_list))

# print(results)


# filter function 
# def is_even(num):
#     return num % 2 == 0

# numbers = [1,2,3,4,5,6]

# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))


#filter out the words which have length greater than 3 


# def word(str):
#     return len(str)>3

# words=["anuj","bashyal","cat"]

# fil=filter(word,words)
# print(list(fil))

#filter out the dictionary item based on some condition like 'name' key length greater than 5
     

# data =[{"name": "Anuj", "age": 24, "city": "Kathmandu"}]

# def name_length(item):
#     return len(item['name'])>5

# filtered_data = filter(name_length, data)
# print(list(filtered_data))


#reduce function
# from functools import reduce 

# def add(x,y):
#     return x + y 

# numbers = [1,2,3,4,5]
# sum_of_numbers = reduce(add, numbers)
# print(sum_of_numbers)


#find the maximum number from the list using reduce function

from functools import reduce

def find_max_with_reduce(numbers):
    maximum = reduce(max, numbers)
    return maximum

my_list = [15, 42, 7, 99, 23]
print(find_max_with_reduce(my_list)) 









    


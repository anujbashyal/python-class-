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


def reverse_output(func):
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)

        if (result, str):
            return result[::-1]
        return result
    return wrapper

@reverse_output
def get_text(name):
    return f"Bashyal {name}"

print(get_text("Anuj"))

def multiplier(factor):
    def multiply_by_factor(number):
        return number * factor
    return multiply_by_factor

multiplier_value = multiplier(5)
print(multiplier_value._name_)




    


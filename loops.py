# for i in range(5):
#     print("hello")

# for i in range(10):
#    print(i)
#    if i % 2 == 0:
#        print(f"even number:{i}")
#        continue
#     print(f"odd number:{i}")


# numbers = [1, "anuj", 75.5, "ronaldo",None, 5]

# for num in numbers:
#    if num==None:
#        print("invalid list")
#        break

#find the smallest element from list

listing = [1,3, 9, 7, 3, 6, 5, 7, 24,798]

smallest=listing[0]
for i in range(1,len(listing)):
    if listing[i] < smallest:
        smallest = listing[i]
print(smallest)

    


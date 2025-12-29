#assi 1
student_scores = {
    "Anuj": [65, 70, 55],
    "Ram": [45, 50, 40]
}

marks = student_scores["Anuj"]

average = sum(marks) / len(marks)

print(average >= 60)

#assi 2
stock = {"apples": 10, "bananas": 2, "oranges": 0}

if "pears" in stock:
    print("yes")
else:
    print("nope")

if "bananas" in stock and stock["bananas"] < 5:
    print("Time to restock bananas")

#assi 3
users = {"admin": "1234"}


users["teacher"] = "password789"


input_user = input("enter a user:")
input_pass = input("enter pass:")


if input_user in users and users[input_user] == input_pass:
    print("Access Granted")
else:
    print("not accessed")



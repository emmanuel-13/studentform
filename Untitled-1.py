
# program to create a simple even number checker

# try:
#     allowed = int(input("enter a value? "))
#     if allowed % 2 == 0:
#         print("Number {} is even".format(allowed))
#     else:
#         print("Number {} is not odd".format(allowed))
# except (ValueError, TypeError, NameError):
#     print("you are not allowed to enter a float or a string")


# Even number checker function
try:
    d = int(input("Enter a number: "))
    if d % 2 == 0:
        print(f"{d} is an even number")
    else:
        print(f"{d} is an odd number")
except ValueError:
    print("Value not a integer ")
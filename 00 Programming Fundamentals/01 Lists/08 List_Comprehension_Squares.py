# 8.	List Comprehension Squares – Create a list of squares of numbers from 1 to n.
n = int(input("Enter a number: "))
squares = [x**2 for x in range(1, n+1)]

print("List of squares:", squares)

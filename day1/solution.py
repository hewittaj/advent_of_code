'''
This Python program solves problem 1 of Advent Of Code for 2020.

In this problem we have to find two numbers that add up to 2020 and then
multiply them together to get the product.
'''
# This will contain the list of numbers we get from the .txt file provided
numbers = [] 

'''
This function populates our variable 'numbers' from the .txt file provided.
This function could be improved upon by allowing a relative path instead of an
absolute path.

First we open the file stored on the computer, and then loop through each line by line.
Each number is then appended to our list as an integer
'''
def populateListOfNumbers(numbers):
    with open("c:\\Users\\h066356\\Documents\\GitHub\\advent_of_code\\day1\\input.txt", 'r') as f:
        for number in f:
            numbers.append(int(number.strip()))

# Method call to populate our list
populateListOfNumbers(numbers)

# Initialize our variable to store the product 
product = 0

'''
Loop through the numbers stored in our list to find what two numbers sum to 2020.
I believe this could be improved upon as right now if the last two numbers are what add to
2020, it is the slowest possible path to get there. I do believe this is an O(n^2) solution.
'''
for num1 in numbers:
    for num2 in numbers:
        if(num1 + num2 == 2020):
            product = num1 * num2

# Finally, we print the product
print(product)

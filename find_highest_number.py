#ask user to input 5 random numbers, and store them in variables

num1 = float(input("Enter the First Number: "))

num2 = float(input("Enter the Second Number: "))

num3 = float(input("Enter the Third Number: "))

num4 = float(input("Enter the Fourth Number: "))

num5 = float(input("Enter the Fifth Number: "))

#assume the first number is the largest. 
#if a number is larger than the current "largest", the "largest" variable is updated

largest = num1 
#we compare the largest with the other variables

if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

if num4 > largest:
    largest = num4

if num5 > largest:
    largest = num5

#output the largest number 

print("The highest number is: ", largest)

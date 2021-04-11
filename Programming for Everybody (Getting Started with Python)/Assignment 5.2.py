#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
#Enter 7, 2, bob, 10, and 4 and match the output below.

'''
Desired output:
Invalid input
Maximum is 10
Minimum is 2
'''
#code
largest = None
smallest = None
nums=[]
while True:
    num = input("Enter a number: ")
    try:
        num=int(num)
        nums.append(num)
        
    except ValueError:
        if num=="done":
            break
        print("Invalid input")
nums.sort()
largest=nums[-1]
smallest=nums[0]
    

print("Maximum is", largest)
print("Minimum is", smallest)
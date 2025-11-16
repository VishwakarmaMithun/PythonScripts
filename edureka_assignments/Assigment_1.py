# Program to check if a number is a palindrome

'''

Input: 121 → Output: Palindrome number

Input: 123 → Output: Not a palindrome number

'''

number = input("enter the number from the user")

if number == number[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

print(number[::-1])



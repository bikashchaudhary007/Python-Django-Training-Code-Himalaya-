'''
#Python-Django Training (Code Himalaya)
Task-1 (26th July 2022)
'''

#To check whether a string is palindrome or not.
def checkPalindrome():
    print("A simple program to check whether a string is palindrome or not.")
    anyString = input("Enter a string: ")
    if(anyString==anyString[::-1]):
        print(f'{anyString} is a palindrome.')
    else:
        print(f"{anyString} is not a palindrome.")

#checkPalindrome()


#To check whether a number is prime number or not.
def checkPrime():
    print("A simple program to check whether a number is prime number or not.")
    num = int(input("Enter any number: "))
    a = 0
    for i in range(1,num+1):
        if num%i == 0:
            a = a + 1

    if a == 2:
        print("It is prime number")
    else:
        print("It is composite number")

#checkPrime()


#To convert a matrix: [[1,2],[3,4],[5,6],[7,8]] into [[1,2,3,5,7],[2,4,6,8]]
def transpose_matrix():
    matrix1 = [[1,2],[3,4],[5,6],[7,8]]
    transposed = [[row[i] for row in matrix1] for i in range (len(matrix1[0]))]
    print(transposed)

#transpose_matrix()

#To count vowels in a string of input. [Using list comprehension]

#Own Logic 
# string = input("Enter any string: ")
# c = 0
# for i in range (0,len(string)):
#     a = string[i].upper()
#     if a =="A" or a =="E" or a =="I" or a =="O" or a == "U":
#         c = c + 1 
# print("Number of vowels:",c)

def countVowels():
    vowel = ['a','e','i','o','u']
    string = input("Enter any string: ")
    c = 0
    for letter in string:
        if letter.lower() in vowel:
            c += 1
    print("vowels: ",c)
#countVowels() 

#From numbers 1 to 100, print "Fizz" if it is multiple of 3 and "Buzz" if it is multiple of 5, "FizzBuzz" if it is multipleof both 3 and 5.
def FizzBuzz():
    a = []
    b = []
    c = []
    for x in range(1,101):
        if x%3==0: 
            a.append(x)
        elif x%5 == 0:
            b.append(x)

        if x%3 == 0 and x%5==0:
            c.append(x)

    print("Fizz numbers are: ",a)
    print("Buzz numbers are: ",b)
    print("FizzBuzz numbers are: ",c)

#FizzBuzz()

#To get the positive numbers in a mix list of string, positive and negative numbers.











 









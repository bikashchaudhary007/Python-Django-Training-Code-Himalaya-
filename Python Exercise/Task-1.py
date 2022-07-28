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

checkPalindrome()


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

checkPrime()


#To convert a matrix: [[1,2],[3,4],[5,6],[7,8]] into [[1,2,3,5,7],[2,4,6,8]]
def transpose_matrix():
    matrix1 = [[1,2],[3,4],[5,6],[7,8]]
    transposed = [[row[i] for row in matrix1] for i in range (len(matrix1[0]))]
    print(transposed)

transpose_matrix()

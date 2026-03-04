'''
#1. 
n = int(input("Enter input: "))
for i in range(n):
    for j in range(n):
        print("*",end = " ")
    print()

#2. Right Angle Triangle
n = int(input("Enter input: "))
for i in range(1, n+1):
    for j in range(i):
        print("*",end =" ")
    print()


#3. Inverted triangle
n = int(input("Enter input: "))
for i in range(1, n+1):
    for j in range(n-i+1):
        print("*",end =" ")
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print("*",end =" ")
    print()

# 4. Number Triangle
n = int(input("Enter number: "))
for i in range(1, n+1):
    for j in range(i):
        print(j+1, end=" ")
    print()


# 5. Repeated number pattern
n = int(input("Enter number: "))
for i in range(1, n+1):
    for j in range(i):
        print(j+1, end=" ")
    print()


#6. Alphabet Triangle
n = int(input("Enter number: "))
for i in range(1, n+1):
    ch = 65
    for j in range(i):
        print(chr(ch+j), end=" ")
    print()

'''

#7. Floyd Triangle
n = int(input("Enter number: "))
for i in range(1, n+1):
    for j in range(i):
        print(j+1, end=" ")
    print()

#8. Hallow square

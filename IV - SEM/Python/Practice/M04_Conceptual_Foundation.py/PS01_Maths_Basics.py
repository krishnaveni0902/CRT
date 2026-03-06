#Basic Arithmetic operator
a = 2
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)


#built-in functions
print(abs(-54))
print(round(5.478))
print(min([10,20,30,40,54,2]))
print(max([10,20,30,40,54,2]))
print(sum([10,20,30,40,54,2]))
print(pow(2,5))
      
import math
print(math.sqrt(81))
print(math.ceil(4.2))
print(math.floor(4.2))
print(math.pi)
print(math.factorial(6))

#find GCD (using math module and using Eucledian method)
a = int(input())
b = int(input())
while b != 0:
    a,b =b, a%b 
print(a)

import math 
a = int(input())
b = int(input())
print(math.gcd(a,b))




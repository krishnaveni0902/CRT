'''
li =[1, 2, 3, 4, 5]
#output: [2,4,6,8,10]
res =[]
for ele in li:
    res.append(ele*2)
print(res)

print([ele* 2 for ele in li])



li = [1,2,3,4,5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)

print([i for i in li if i%2 == 0])
print(tuple(i for i in li if i%2 == 0))
print({i:i*2 for i in li if i%2 == 0})



li1 = ['a','b','c']
#"a b c"
res = " "
for ch in li1:
    res = res + ch + " "
print(res)

print(" ".join(li1))
'''

'''
#Pyramid

Output:
     * 
    * *
   * * *
  * * * * 
  
n = int(input("Enter a number: "))
for i in range(1, n+1):
        print(" "*(n-i)+ "* "*i)
'''
#Inverted pyramid
n = int(input())
for i in range(n, 0, -1):
        print(" "*(n-i)+ "* "*i)

n = int(input())
for i in range(1, n+1):
        print(" "*(n-i) + "* "*i)
    
#5. Palindrome Pattern
1
212
32123
4321234
  
n = int(input())
for i in range(n, 0, -1):
        print()
        
'''
a = [10,20,30,40.52]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i] + a[j])    #O(n^2)

why optimization is important:
--> Improves progress speed
--> Reduces the memory usage
'''

a = [10, 20, 30, 40, 52]
sum1 = 0
for i in range(len(a)):
    sum1 += a[i]                         #O(n)
print(sum1)

a = [10, 20, 30, 40, 52]
print(sum(a))                          

a = print([i*i for i in range(10)])    

#find the max ele in the list
a = []




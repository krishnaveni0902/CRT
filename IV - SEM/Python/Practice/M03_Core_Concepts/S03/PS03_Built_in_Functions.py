#1. Largest number (using max()) --> largest value un list
arr = [1, 2, 3, 4, 5]
print(max(arr))

#2. check palindrome (using reversed() & join()) --> joins a list of string into single line
word = 'madam'
if word == "".join(reversed(word)):
    print("Palindrome")
else:
    print("Not a palindrome")

#3. count even numbers (using filter()) --> filters elements based on a condition
arr = [ 1, 4, 2, 7, 8, 5, 10]
res = list(filter(lambda x:x%2 == 0, arr))
print(res)

#4. Remove duplicate (using set()) --> unique collection of data
arr = [ 1, 4, 3, 5, 4, 2]
print(set(arr))

#5. sum of digits Alphabetically (using sorted()) --> sorts a list of words in alphabetical order
num = 52941

digits = list(str(num))
sorted_digits = sorted(digits)
total = sum(int(d) for d in digits)

print("Sorted digits:", sorted_digits)
print("Sum of digits:", total)

#7. find common elements (using set())
a = set([10, 25, 48, 9, 7, 8])



#8. Index with Value (using enumerate())  --> adds a index to each element while iterating




#9. Pair two lists (using zip()) --> combines multiple iterable ele - wise

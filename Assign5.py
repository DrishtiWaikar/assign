ls=[1,2,3,8,6,7,5,10,26,4]
print("Sum is:", sum(ls))
print("Largest Number is:", max(ls))
print("Smallest Number is:", min(ls))
ls.sort()
print("Ascending Order is:",ls)
ls.sort(reverse=True)
print("Descending Order is:",ls)
t=tuple(ls)
print("Tuple:", t)
del ls
print()
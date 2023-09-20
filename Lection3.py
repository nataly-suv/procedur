div =5 
arr= [i for i in range(100)]
el = lambda x: x % div
print(list(map(el, arr)))
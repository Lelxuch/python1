from itertools import permutations
 
def func(arr):
    ans = permutations(arr)
    for i in list(ans):
        print (i)

arr = ['a', 'b', 'c'];
func(arr)
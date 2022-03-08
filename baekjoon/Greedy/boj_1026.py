def getMinS(arr1,arr2) :
    result = 0
    for i in range(len(arr1)):
        tmp_a = arr1.pop(arr1.index(min(arr1)))
        tmp_b = arr2.pop(arr2.index(max(arr2)))
        result += tmp_a * tmp_b
    return result
    
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(getMinS(a,b))

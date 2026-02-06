arr = [1,2,3,4,5,6,7]
k = 7
result = []
def combination(index, target, path):
    
    if index == len(arr):
        if target == 0:
            result.append(path.copy())
        return

    #not considering the element
    combination(index+1, target, path)

    # considering the element
    if arr[index] <= target:
        path.append(arr[index])
        combination(index, target-arr[index], path) 
        path.pop()
        target-arr[index]

combination(0, k, [])
print(result)
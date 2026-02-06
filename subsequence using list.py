num = ['1','2','3', '4']
result = []

def subsequence(input, path, index):
    if index == len(input):
        result.append(path.copy())
        return

    #skip the element at current index
    subsequence(input, path, index+1) 
    
    #consider the element at current index
    path.append(input[index])
    subsequence(input, path, index+1)

    #backtrack by poping from path
    path.pop()



subsequence(num, [], 0)
print(result) 
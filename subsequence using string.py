num = "Anu"
result = []

def subsequence(input, path, index):
    if index == len(input):
        result.append(path)
        return

    #skip the element at current index
    subsequence(input, path, index+1) 
    
    #consider the element at current index
    subsequence(input, path+input[index], index+1)


subsequence(num, '', 0)
print(result) 
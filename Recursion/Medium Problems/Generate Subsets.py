
def helper(slate:list, i, array, result:list):
    if len(array) == i:
        result.append(slate.copy())
        return
    else:
        # exclude
        helper(slate, i+1, array, result)
        
        #include
        slate.append(array[i])
        helper(slate, i+1, array, result)
        slate.pop()
        

def generate_all_subsets(s):
    # print(s, list(s))
    result = []
    slate = []
    helper(slate, 0, list(s['s']), result)
    return result



print(generate_all_subsets({
"s": "xywer"
}
))
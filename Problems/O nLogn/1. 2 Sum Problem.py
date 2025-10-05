def pair_sum_sorted_array(numbers, target):
    res = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == target:
                res.append([numbers[i],numbers[j]])
                
    if len(res) == 0:
        return [-1,-1]
    else:
        return res


print(pair_sum_sorted_array([1, 2, 3, 5, 10], 7))
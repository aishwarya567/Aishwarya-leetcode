#input = [4,7,2,10] and target = 14
#Output = [0, 3] --> return the index of the added two numbers i.e 10+4 = 14

def TwoSum(num, target):
    empty_dict = {}
    for i in range(0, len(num)):
        empty_dict[num[i]] = i
    for i in range(0, len(num)):
        res = target - num[i]
        if res in empty_dict and i != empty_dict[res]:
            return [i, empty_dict[res]]
    return None
pos = TwoSum([4,7,2,10], 14)
pos1 = TwoSum([4, 7, 2, 10], 12)
print(pos)
print(pos1)

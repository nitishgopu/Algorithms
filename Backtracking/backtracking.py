
#Get all subsets
def subset(nums):
    
    tmp = []
    list = []
    soln = backtrack(list,tmp,nums,0)
    return soln

def backtrack(list,tmp,nums,k):

    list.append([n for n in tmp])

    for k in range(k,len(nums)):
        tmp.append(nums[k])
        backtrack(list,tmp,nums,k+1)
        tmp.pop()

    return list


# Combination sum without using the same number.
def combinationsum(nums,target):

    nums.sort()
    tmp = []
    list = []
    soln = backtrackComb(list,tmp,nums,0,target)
    return soln

def backtrackComb(list,tmp,nums,k,target):

    if (target < 0): return;

    if target == 0:
        list.append([n for n in tmp])

    for k in range(k,len(nums)):
        tmp.append(nums[k])
        backtrackComb(list,tmp,nums,k+1,target-nums[k])
        tmp.pop()

    return list



inp = [1,2,3,5,4]
target = 5
#combinationsum(inp,target)
#subset(inp)


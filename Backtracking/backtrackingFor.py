




def subset(nums,target):

    #nums.sort()

    tmp = []
    list = []
    ans = backtrack(list,tmp,nums,0)
    print ans

def backtrack(list,tmp,nums,k):

    list.append([n for n in tmp])

    for k in range(k,len(nums)):
        tmp.append(nums[k])
        backtrack(list,tmp,nums,k+1)
        tmp.pop()

    return list


def combinationsum(nums,target):

    #nums.sort()

    tmp = []
    list = []
    ans = backtrackComb(list,tmp,nums,0,target)
    print ans

def backtrackComb(list,tmp,nums,k,target):
    #print k,tmp

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
combinationsum(inp,target)
#subset(inp,target)


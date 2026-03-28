## pairs
nums = list(map(int,input().split()))
pairs = [(i,j) for i in nums for j in nums]
print(pairs)

## unique pairs
unique_pairs = [(nums[i],nums[j])
                for i in range(len(nums))
                for j in range(i+1,len(nums))]
print(unique_pairs)

unique = list(set(nums))
print(unique)
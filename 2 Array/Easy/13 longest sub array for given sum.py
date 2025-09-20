# # Input Format: 
# n = 5 
# k = 5
# arr = [2,3,5]

# arr.sort()
# print(arr)

# i=0
# sum=0
# count=0
# iter=0
# while(k!=sum):
#     if sum>k:
#         print("here")
#         iter+=1
#         i=iter
#         sum=0
#         count=0
#     if sum==k:
#         print(sum)
#     sum+=arr[i]
#     count+=1
#     i+=1


# print("final",count)




from typing import List

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: Sum += a[right]

    return maxLen


if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")
"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""

def largestDivisibleSubset(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""	
	if not nums:
		return []
	nums.sort()
	subsets =  [[num]for num in nums]
	for i in range(len(nums)):
		for j in range(i):
			# print(f'nums[i]: {nums[i]} nums[j] {nums[j]}')
			if nums[i] % nums[j] == 0 and len(subsets[i]) <= len(subsets[j]):
				# print(f'nums[i]: {nums[i]} nums[j] {nums[j]}')
				subsets[i] = [nums[j]] + subsets[i]
	print(subsets)
	return max(subsets, key=len)	


def main():
	A = [1,2,4,8]
	B = [1,2,3]
	print(largestDivisibleSubset(A))
	print(largestDivisibleSubset(B))


if __name__ == '__main__':
	main()

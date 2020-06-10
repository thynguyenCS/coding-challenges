"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0

My approach:
- Checking if target a member of nums => return index using method index(target)
- Else searching the index to insert using binary search 
"""
def searchInsert(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	if target in nums:
		return nums.index(target)
	else:
		return binary_search(nums, target)


def binary_search(arr, elem):
	start = 0
	end = len(arr)
	while(start < end):
		mid = (start + end)//2
		if elem < arr[mid]:
			end = mid
		elif elem > arr[mid]:
			start = mid + 1
	return start



def main():
	arr = [1,3,5,6]
	print(searchInsert(arr, 5))  # 2
	print(searchInsert(arr, 2))  # 1
	print(searchInsert(arr, 7))  # 4
	print(searchInsert(arr, 0))  # 0


if __name__ == '__main__':
	main()
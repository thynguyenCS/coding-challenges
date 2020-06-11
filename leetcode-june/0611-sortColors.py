"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of 
the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

My approach:
Similar to selection sort. But we do not need to go through the whole array, since there is only 3 values: 0,1,2. 
Setting up 3 cursors: start, current and end
For each index of array:
value of 0: swap arr[current] with arr[start], and increment these 2 cursors
value of 1: increase current cursor
value of 2: swap arr[current] with arr[end], decrease end cursor
"""

def sortColors(nums):
	"""
	:type nums: List[int]
	:rtype: None Do not return anything, modify nums in-place instead.
	"""
	if not nums:
		print("List is empty. Nothing to sort")
	else:
		start, cur, end = 0, 0, len(nums) - 1
		while cur <= end:
			if nums[cur] == 0:
				nums[start], nums[cur] = nums[cur], nums[start]
				start += 1
				cur += 1
			elif nums[cur] == 1:
				cur += 1
			else: 
				nums[cur], nums[end] = nums[end], nums[cur]
				end -= 1
	print(nums)


def main():
	sortColors([2,0,2,1,1,0])
	sortColors([2,0,1])
	sortColors([0,1,2,0,1,2,2,2,0,0,1,2])


if __name__ == '__main__':
	main()

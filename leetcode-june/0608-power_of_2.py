"""
@author: Thy Nguyen
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 2^0 = 1
Example 2:

Input: 16
Output: true
Explanation: 2^4 = 16
Example 3:

Input: 218
Output: false

My approach: binary approach
Recognize:
1 = 00000001
2 = 00000010
4 = 00000100
8 = 00001000
and so on

So a number is a number of 2 has only one 1 appearing in its binary representation
If subtract 1 from those number, we have:
1 - 1 = 00000000
2 - 1 = 00000001
4 - 1 = 00000011
8 - 1 = 00000111
and so on

Using & operation:
2 & 1 = 0
4 & 3 = 0
8 & 7 = 0 
and so on
"""

def isPowerOfTwo(num):
	"""
	:type n:int
	:rtype: bool
	"""
	return num != 0  and (num & (num-1)) == 0 


def main():
	isPowerOfTwo(4)


if __name__ == '__main__':
	main()
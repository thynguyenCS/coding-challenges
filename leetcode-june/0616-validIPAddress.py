"""
Valid IP Address

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

***IPv4 addresses are canonically represented in dot-decimal notation, 
which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

***IPv6 addresses are represented as eight groups of four hexadecimal digits, 
each group representing 16 bits. The groups are separated by colons (":"). 
For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. 
Also, we could omit some leading zeros among four hexadecimal digits and 
some low-case characters in the address to upper-case ones, 
so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address
(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group 
using two consecutive colons (::) to pursue simplicity. 
For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. 
For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
"""
import string
def validIPv4(ip):
	'''
	- need to have exactly 4 groups
	- each group:
		cannot have leading 0
		between 0 and 255
		digit only
	'''
	notations = ip.split(".")
	if len(notations) != 4:
		return False
	for num in notations:
		if not num:
			return False
		#print(num)
		if num[0] == '0' and len(num)>1:
			#print("invalid")
			return False
		if not num.isdigit():
			return False
		if int(num) < 0 or int(num)>255:
			return False
	return True


def validIPv6(ip):
	'''
	- need to have exactly 8 groups
	- each group:
		have 1-4 alphanumeric characters
	'''
	groups = ip.split(":")
	# print(len(groups))

	if len(groups) != 8: 
		return False
	for group in groups:
		# print(group)
		# if group[0] == '0' and len(group)>1:
		# 	print("leading 0")
		# 	return False
		if len(group) < 1 or len(group) > 4: 
			# print("len")
			return False
		for digit in group:
			if digit not in string.hexdigits:
				# print("alphanumeric")
				return False
	return True


def validIP(ip):
	if validIPv4(ip):
		return "IPv4"
	elif validIPv6(ip):
		return "IPv6"
	else:
		return "Neither"

def main():
	ip1 = "2001:db8:85a3:0:0:8A2E:0370:7334"
	ip2 = "02001:0db8:85a3:0000:0000:8a2e:0370:7334"
	ip3 = "2001:0db8:85a3::8A2E:0370:7334"


	print(validIP(ip1))
	print(validIP(ip2))
	print(validIP(ip3))



if __name__ == '__main__':
	main()
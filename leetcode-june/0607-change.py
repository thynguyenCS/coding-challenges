#------------------------------------------------------------
# @author: thynguyen
#------------------------------------------------------------
"""
Problem: Coin Change 2
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin. 

Example 1: 
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2: 
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Approach:
Create a 2d array to keep track all the possible ways for coin change
Return max value of entries
Example 1
	0	1	2	3	4	5 <---- total amount
0
1
2
3
^
|
array coins

Initial first row with 0s and first columns with 1s
	0	1	2	3	4	5
0	1	0	0	0	0	0
1	1
2	1
3	1

If the coins[index] < amount => no update

Coin value of 1:
How many ways do we have change from coin 1 for total amount of 1: 1; 2: 1 and so on
	0	1	2	3	4	5
0	1	0	0	0	0	0
1	1	1	1	1	1	1
2	1
3	1

Coin value of 2:
	0	1	2	3	4	5
0	1	0	0	0	0	0
1	1	1	1	1	1	1
2	1	1	2	2	3	3
3	1
Amount 1: There is only 1 way (amount(1)< coin value(2), no update, = array[2][1])
Amount 2: 1 way (array[1][2]) + 1 way (array[2][2-2])
Amount 3: 1 way (array[1][3]) + 1 way (array[2][3-2])
Amount 4: 1 way (array[1][4]) + 2 way (array[2][4-2])
Amount 5: 1 way (array[1][5]) + 1 way (array[2][5-3])


Coin value of 5:
	0	1	2	3	4	5
0	1	0	0	0	0	0
1	1	1	1	1	1	1
2	1	1	2	2	3	3
3	1	1	2	2	3	4
From Amount 1-4: amount< coin value, repeat number of ways from previous row
Amount 5: 3 way (array[2][5]) + 1 way (array[3][5-5]) = 4
return array[coins.size][amount]


"""

def change(amount, coins):
	"""
	:type amount: int
	:type coints: List[int]
	:rtype: int
	"""
	# initial the 2d-array like explained above
	dp = [[1] + [0]*amount for i in range(len(coins) +1)]

	# looping though the array and adding the number of ways
	for row in range(1, len(coins)+1):
		for col in range(1, amount+1):
			# print(f'row: {row} col: {col}')
			if coins[row - 1] > col:
				dp[row][col] = dp[row -1][col]
			else:
				dp[row][col] = dp[row -1][col] + dp[row][col-coins[row-1]]
	return dp[-1][-1]


def main():
	print(change(5,[1,2,5]))



if __name__ =="__main__":
	main()

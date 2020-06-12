"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. 
Each element must have the same probability of being returned.

Example:
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
import random
class RandomizedSet():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
        	return False 
        else:
        	self.data.append(val)
        	return True 

        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
        	self.data.remove(val)
        	return True     
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        random_idx = random.randint(0, len(self.data)-1)
        return self.data[random_idx]



def main():
	obj = RandomizedSet()
	print(obj.insert(1))  # True
	print(obj.insert(1))  # False
	print(obj.insert(2))  # True
	print(obj.insert(4))  # True
	print(obj.getRandom())



if __name__ == '__main__':
	main()
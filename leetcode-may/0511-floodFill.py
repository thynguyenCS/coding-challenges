"""
Problem:
An image is represented by a 2-D array of integers, each integer representing the pixel value of 
the image (from 0 to 65535). Given a coordinate (sr, sc) representing the starting pixel (row and column)
of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to 
the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally 
to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all 
of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

Hint #1  
Write a recursive function that paints the pixel if it's the correct color, then recurses on neighboring pixels.
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        color = image[sr][sc]
        if color == newColor:
            return image
        self.dfs(image, sr, sc, color, newColor)
        return image
        
    def dfs(self, image, r, c, color, newColor):
        """
        :type image: List[List[int]]
        :type r: int
        :type c: int
        :type color: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1: 
                self.dfs(image, r-1, c, color, newColor)
            if r+1 < len(image): 
                self.dfs(image, r+1, c, color, newColor)
            if c >= 1: 
                self.dfs(image, r, c-1, color, newColor)
            if c+1 < len(image[0]): 
                self.dfs(image, r, c+1, color, newColor)

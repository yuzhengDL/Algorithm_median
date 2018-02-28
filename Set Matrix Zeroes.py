/*
思路：先遍历整个matrix，分别使用row和col两个数组记录下当前行或列是否存在0；其次扫描row和col，只要某一行或是某一列存在0，将其置为0.
该算法需要额外的O(m+n)的空间。
*/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        row = [False] * len(matrix)
        col = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in range(len(row)):
            for j in range(len(col)):
                if row[i] or col[j]:
                    matrix[i][j] = 0
             
/*
思路：把matrix的第一行第一列作为前面的数组row和col，用来记录各行各列是否有0，算法流程如下：
- 先扫描第一行第一列，如果有0，则将各自的flag设置为true
- 然后扫描除去第一行第一列的整个数组，如果有0，则将对应的第一行和第一列的数字赋0
- 再次遍历除去第一行第一列的整个数组，如果对应的第一行和第一列的数字有一个为0，则将当前值赋0
- 最后根据第一行第一列的flag来更新第一行第一列
*/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        fr = False; fc = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                fc = True
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                fr = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if fc:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if fr:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0              

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix)

        while (lo < hi):
            m = math.floor((hi - lo) / 2) + lo

            firstN = matrix[m][0]
            
            if (firstN == target):
                return True
            
            if (firstN > target):
                hi = m
            
            if (firstN < target):
                if (target <= matrix[m][len(matrix[m]) - 1]):
                    f = 0
                    l = len(matrix[m])
                    while (f < l):
                        c = math.floor((l - f) / 2) + f
                        if (matrix[m][c] == target):
                            return True
                        
                        if (matrix[m][c] > target):
                            l = c

                        if (matrix[m][c] < target):
                            f = c + 1

                    return False
                
                else:
                    lo = m + 1


        return False

        
class Solution(object):
    def spiralOrder(self, matrix):
        out = []
        while matrix:
            out+=(matrix.pop(0))
            if matrix and matrix[0]:
                for row in matrix:
                    out.append(row.pop())
            if matrix :
                out+=(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    out.append(row.pop(0))
        return out
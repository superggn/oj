"""
https://www.lintcode.com/problem/1179/
"""
from collections import deque


class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """

    def findCircleNum(self, mat):
        cnt = 0
        for stu in range(len(mat)):
            if mat[stu][stu] == 1:
                cnt += 1
                self.BFS(stu, mat)
        return cnt

    def BFS(self, stu, mat):
        queue = deque([stu])
        while queue:
            stu = queue.popleft()
            mat[stu][stu] = 2
            for other in range(len(mat[0])):
                if mat[stu][other] == 1 and mat[other][other] == 1:
                    queue.append(other)
        return

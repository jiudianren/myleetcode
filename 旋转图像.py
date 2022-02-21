class Solution:
    def rotate(self, matrix: list) -> list:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for kuan in range(n,0,-2):
            # 层循环
            row = (n-kuan)//2 # 当前外圈的所在的行列
            col = row

            for i in range(kuan-1):
                # 边循环
                print(f"kuan,{kuan},i,{i}")
                r_index = row
                c_index = col + i
                print(f"r,k :{r_index},{c_index}")
                temp = matrix[r_index][c_index]
                for this_time in range(4):
                    #每个数字旋转四次
                    next_r = c_index
                    next_c = n-1-r_index
                    print(f"{this_time}, {r_index},{c_index}-->{next_r},{next_c}")
                    print(f"b:{matrix[r_index][c_index]},{matrix[next_r][next_c]},tmp：{temp}")
                    matrix[r_index][c_index] = matrix[next_r][next_c]
                    matrix[next_r][next_c] = temp
                    temp = matrix[r_index][c_index]
                    print(f"a:{matrix[r_index][c_index]},{matrix[next_r][next_c]}")
                    print(matrix)
                    r_index = next_r
                    c_index =next_c

        return matrix

    def t(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        matrix = [[1, 2, 3,4,17],
                  [5, 6,7,8,18],
                  [9,10,11,12,19],
                  [13,14,15,16,20],
                  [21, 22, 23, 24, 25],
                  ]
        cpaa= matrix[:]
        print(self.rotate(matrix))
        print(cpaa)




if __name__ == "__main__":
    Solution().t()

from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        rows,cols= len(img),len(img[0])
        ans=[[0]* cols for _ in range(rows) ]

        direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


        
        for i in range(rows) :
            for j in range(cols) :
                sum_cels=0
                count=0
                for dx,dy in  direction:
                    nx,ny=i+ dx,j+dy 

                    if  0<= nx <rows and  0<= ny <cols:
                        sum_cels +=img[nx][ny]
                        count+=1

                ans[i][j]=sum_cels//count
        return ans 




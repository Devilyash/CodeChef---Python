class Solution:
    def solve(self, pc, pr):
        if pc%9 == 0:
            chef = pc//9
        else:
            chef = pc//9 + 1
        if pr%9 == 0:
            rick = pr//9
        else:
            rick = pr//9 + 1
            
        if chef < rick:
            print(0, end=" ")
            print(chef)
        elif chef > rick:
            print(1, end=" ")
            print(rick)
        else:
            print(1, end=" ")
            print(rick)

    
obj = Solution()
t = int(input())
for i in range(t):
    pc, pr = map(int, input().split())
    obj.solve(pc, pr)


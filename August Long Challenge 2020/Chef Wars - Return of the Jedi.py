class Solution:
    def whoWillDie(self, h, p):
        #h = health of Darth, #p = power of chef's lightsaber
        if h <= p:
            print(1)
            return
        elif h == 0:
            print(1)
            return
        elif p == 0:
            print(0)
            return
        self.whoWillDie(h-p, p//2)
        
obj = Solution()
t = int(input())
for i in range(t):
    h,p = map(int, input().split())
    obj.whoWillDie(h,p)

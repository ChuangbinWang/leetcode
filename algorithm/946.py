class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                j += 1
                stack.pop()
        return j == len(popped)
        # 这一题好像开保险柜锁的原理，poped 数组就是 锁， pushed就是钥匙，当我们找到 我们的pushed数组中与锁第一个匹配的位置时就往回转，把顺序相同的内容 推出来，然后去找下一个匹配的位置。
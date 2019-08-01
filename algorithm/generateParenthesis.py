class Solution:
    def generateParentheis(self, n:int)->List[str]:
        self.ret_list = []
        self._gen(0,0,n,"")
        return self.ret_list
    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.ret_list.append(result)
            return
        if left < n:
            self._gen(left + 1, right, n - 1, result + '(')
        if left > right and right < n:
            self._gen(left, right + 1, n - 1, result + ')')
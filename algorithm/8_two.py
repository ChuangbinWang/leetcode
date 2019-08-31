class Solution(object):
    def myAtoi(self, str):
        str = str.lstrip()
        if len(str) == 0:
            return 0
        i = 2
        if str[0] == '-' or str[0] == '+':
            i = 2
        else:
            i = 1
        num = 0
        while i <= len(str):
            try : 
                num = int(str[:i])
                i += 1
            except:
                break
        if num < -2147483648 :
            return -2147483648
        if num > 2147483647:
            return 2147483647
        return num
if __name__ == "__main__":
   str = "  - 421"
   out = Solution().myAtoi(str)
   print out

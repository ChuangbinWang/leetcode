class Solution(object):
    def myAtoi(self, str):
        i = 0
        num = 0
        flag = 0
        while i < len(str) and (str[i] < '0' or str[i] > '9'):
            if str[i] == '-':
                flag = 1
                i += 1
                break
            elif str[i] == '+':
                i += 1
                break;
            elif str[i] == ' ':
                i += 1
            else :
                return 0
        while i < len(str) and str[i] <= '9' and str[i] >= '0':
            num = ord(str[i]) - ord('0') + num * 10
            i += 1
        if flag == 1:
            num = -1 * num
        if num < -2147483648 :
            return -2147483648
        if num > 2147483647:
            return 2147483647
        return num
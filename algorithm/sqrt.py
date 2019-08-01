class Solution:
    def mySqrt(self, x: int) -> int:
        # Ϊ���չ˵� 0 ����߽�����Ϊ 0
        l = 0
        # Ϊ���չ˵� 1 ���ұ߽�����Ϊ x // 2 + 1
        r = x // 2 + 1
        while l < r:
            # ע�⣺����һ��ȡ����λ�������ȡ����λ����������ܻ������ѭ��
            mid = l + (r - l + 1) // 2
            square = mid * mid
            
            if square > x:
                r = mid - 1
            else:
                l = mid
        return l
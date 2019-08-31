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
        # ��һ����񿪱��չ�����ԭ��poped ������� ���� pushed����Կ�ף��������ҵ� ���ǵ�pushed������������һ��ƥ���λ��ʱ������ת����˳����ͬ������ �Ƴ�����Ȼ��ȥ����һ��ƥ���λ�á�
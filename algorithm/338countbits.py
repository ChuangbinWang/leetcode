class Solution:
    def countBits(self, num: int) -> List[int]:
        target = []
        target.insert(0, 0)
        for i in range(1,num + 1):
            target.insert(i, target[i & (i-1)] + 1)
        return target

# class Solution {
#     public int[] countBits(int num) {
#         int[] res = new int[num +1];
#         for (int i = 1; i <= num; i++){
#             res[i] = res[i&(i-1)]+1
#         }
#         return res;
            
#     }
# }
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        repeticao = {}
        for num in nums:
            if num in repeticao:
                repeticao[num] += 1
            else:
                repeticao[num] = 1
        for num, contagem in repeticao.items():
            if contagem % 2 != 0:
                return False
        return True

nums = [3, 2, 3, 2, 2, 2]
solucao = Solution()
print(solucao.divideArray(nums))
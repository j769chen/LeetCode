class Solution:
    # Find the products up to each elt in the array including itself both forwards and backwards.
    # the 2nd elt in the backwards products array is the answer for idx 0,
    # the 2nd last elt in the fwds product array is the answer for the last idx
    # for the rest, the answer is fwdProducts at index to the left * bwdProducts at the index to the right.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwdProducts = [0 for i in range(len(nums))]
        bwdProducts = [0 for i in range(len(nums))]
        solArr = [0 for i in range(len(nums))]

        fwdProducts[0] = nums[0]
        bwdProducts[-1] = nums[-1]

        for i in range(1, len(nums)):
            fwdProducts[i] = nums[i]*fwdProducts[i-1]

        for i in range(len(nums)-2, 0, -1):
            bwdProducts[i] = nums[i]*bwdProducts[i+1]

        solArr[0] = bwdProducts[1]
        solArr[-1] = fwdProducts[len(nums)-2]

        for i in range(1, len(nums)-1):
            solArr[i] = fwdProducts[i-1] * bwdProducts[i+1]
        
        return solArr

        
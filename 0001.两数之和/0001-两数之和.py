class Solution(object):
    def twoSum(self, nums, target):
        '''
        Hashmap  
        The best solution
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            dic[num] = i 

class Solution2 (object):
    '''
    Brute Force 
    The worst solution
    Time Complexity : O(n^2)
    Space Complexity : O(1)
    '''
    # def twoSum(self,nums1:list, target1:int) -> list:
    def twoSum(self,nums1:list, target1:int):
        for i in range(len(nums1)):
            for j in range( i+1, len(nums1)) :
                if nums1[i] + nums1[j] == target1:
                    return [i,j]


a2 = Solution2()
b2 = a2.twoSum([1,2,3,4,5,6,7,8,9], 16)

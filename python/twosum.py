
from typing import List

class Solution:
	def twoSumBrute(self, nums: List[int], target: int) -> List[int]:
	for firstIndex in range(len(nums)):
		for secondIndex in range(firstIndex + 1, len(nums)):
			if firstIndex != secondIndex and nums[firstIndex] + nums[secondIndex] == target:
				return [firstIndex, secondIndex]

    def twoSumTwoPass(self, nums: List[int], target: int) -> List[int]:
        values_seen = {}
        for index in range(len(nums)):
            values_seen[nums[index]] = index
        
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in values_seen and values_seen[complement] != index:
                return [index, values_seen[complement]]

    def twoSumOnePass(self, nums: List[int], target: int) -> List[int]:
    	values_seen = {}
    	for index in range(len(nums)):
    		complement = target - nums[index]
    		if complement in values_seen and values_seen[complement] != index:
    			return [index, values_seen[complement]]
    		values_seen[nums[index]] = index


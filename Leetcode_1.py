class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = dict()
        for idx, key in enumerate(nums[:]):
            hashmap[key] = idx

        for idx, key in enumerate(nums[:]):
            target1 = target - key
            if target1 in hashmap and hashmap[target1] != idx:
                result.append(idx)
                result.append(hashmap[target1])
                return result
        return result
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        largest_count = 0
        total = 0

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in freq:
            if freq[i] > largest_count:
                largest_count = freq[i]
                total = freq[i]
            elif freq[i] == largest_count:
                total += freq[i]

        return total
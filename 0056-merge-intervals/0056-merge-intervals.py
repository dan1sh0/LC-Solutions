class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # in order to check if intervals are merging
        # we can check if the second number is greater than the first number of the second list 
        # if so we can merge by creating a new list that would have the first number of the first list and the last number of the second list 
        # we continue to check like that and just append to the new list 
        # from initial thoughts, this would be o(n)^2 runtime 
        # as we would have nested for loops
        
        # edge case: are they sorted? 
        # what if its empty 
        
        # so we can sort the array which allows us to write an o(n) algorithm 
        # overall time complexity will be O(log (n) * n) since we are sorting 
        
        intervals.sort(key = lambda x:x[0])
        
        merge = []
        
        # then we loop through the array
        for interval in intervals:
            # if the array is empty or the last number in the first array is less than the first number in the second array then it doesnt overlap so we just append 
                #m   i
            # [1,3] [2,6]
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                # otherwise make the last number in the first array the max of that and the last number in the second array to merge the intervals 
                merge[-1][1] = max(merge[-1][1], interval[1])
        return merge 
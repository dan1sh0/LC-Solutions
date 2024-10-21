class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # we will create an additonal array to store the res 
        # we can have two pointers one starting at word1 and the other at word2 
        # then we append from the first word and then the second, 
        # and the end if we still have remaining of the word, then just append the rest 
        
        
        
        res = []
        p1, p2 = 0, 0 
        
        # we create the two pointers and continue to append until they reach the end 
        # time complexity = O(word1 * word2), at worst case we would have to go to the end of both word 1 and word2 
        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                res+=word1[p1]
                p1+=1
            if p2 < len(word2):
                res+=word2[p2]
                p2+=1
        
        return "".join(res)
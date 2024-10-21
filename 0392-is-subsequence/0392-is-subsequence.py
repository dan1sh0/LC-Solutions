class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # we can have two pointers 
        # one at s and another at t 
        # we check if char is equal to each other at both s and t 
        # if it is we increment both pointers and continue 
        # if they are not equal we just increment t, and continue 
        # if we are able to reach the end of both strings we return True 
        # if we could not, return False 
        
        # Time Complexity is O(n) where n is the length of t  
        char1, char2 = 0, 0 
        
        while char1 < len(s) and char2 < len(t):
            if s[char1] == t[char2]:
                char1+=1
                char2+=1
            else:
                char2+=1
            
        return len(s) == char1
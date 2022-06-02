class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict={}
        for i,ele in enumerate(magazine):
            if ele in dict:
                dict[ele]=dict[ele]+1
            else:
                dict[ele]=1
        for i,ele in enumerate(ransomNote):
            if ele in dict and dict[ele]>0:
                dict[ele]=dict[ele]-1
            else:
                return False
        return True
    
#Input: ransomNote = "a", magazine = "b"
#Output: false

#Input: ransomNote = "aa", magazine = "ab"
#Output: false
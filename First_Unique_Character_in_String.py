class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
                  
        for i,ele in enumerate(s):
            if ele in dict:
                dict[ele]=dict[ele]+1
            else:
                dict[ele]=1
        print(dict)
        for i,ele in enumerate(s):
            if dict[ele]==1:
                return i
        return -1
    
    
        
#Input: s = "leetcode"
#Output: 0

#Input: s = "loveleetcode"
#Output: 2
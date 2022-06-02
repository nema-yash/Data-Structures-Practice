class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        if len(s)!=len(t):
            return False
        
        for i,ele in enumerate(s):
            if ele in dict:
                dict[ele]=dict[ele]+1
            else:
                dict[ele]=1
        
        for i,ele in enumerate(t):
            if ele in dict:
                dict[ele]=dict[ele]-1
            else:
                return False
        print(dict)
        
        for k in dict.values():
            print(k)
            if k>0:
                return False
        return True
                
        
#Input: s = "anagram", t = "nagaram"
#Output: true

#Input: s = "rat", t = "car"
#Output: false        
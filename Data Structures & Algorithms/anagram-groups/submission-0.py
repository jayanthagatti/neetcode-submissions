class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=dict()
        # hashmap<string, >
        for i in strs:
            temp=i
            temp=(list)(temp)
            temp.sort()
            temp=str(temp)
            # Arrays.toString(temp)
            #key
            if temp in h.keys():
                h[temp].append(i)
            else:
                h[temp]=[]
                h[temp].append(i)
                #h.get(temp).add(i)
            
        ans=[]
        for i in h.values():
            ans.append(i)
        return ans
        
        
        

        
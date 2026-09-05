class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val={}
        for i in nums:
            if i in val:
                val[i]+=1 
            else:
                val[i]=1 
        

        return sorted(val,key=lambda x:val[x],reverse=True)[:k]
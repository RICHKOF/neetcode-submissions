class Solution:

#encode- turn standardised normal everyday language into ASCII or other ways a comp can understand
# decode convert code back into language we understand 
# use a function in order to first encode and do the same for decoding it back 
# use a loop to go through a string 
#converts that string back into numbers


  
    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+= str(len(s))+"#"+ s 
        return res 
      

        
     
    def decode(self, s: str) -> List[str]:
 
        res,i=[],0 

        while i < len(s):
          j=i
          while s[j]!="#":
             j+=1
          length= int(s[i:j])  
          res.append(s[j + 1: j + 1 + length])
          i= j+1 + length 
        return res


    

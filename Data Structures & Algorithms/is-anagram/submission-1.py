class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1={}
        dictionary2={}
        cond1=True
        cond2=True
        for i  in s:
            if dictionary1.get(i,False):
                dictionary1[i]=dictionary1[i]+1
            else:
                dictionary1[i]=1
        for k  in t:
            if dictionary2.get(k,False):
                dictionary2[k]=dictionary2[k]+1
            else:
                dictionary2[k]=1
        #print(dictionary1)
        # print(dictionary2)
        
        for j in s:
            if dictionary1[j]!=dictionary2.get(j,False):
                cond1=False
       
        for l in t:
            if dictionary2[l]!=dictionary1.get(l,False):
                cond2=False
        if cond1==True and cond2==True:
            return True
        else:
            return False

        
        
    
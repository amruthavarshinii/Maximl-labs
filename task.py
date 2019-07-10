def max_char(str,n):
    count=[0]*256
    for i in range(n):
        count[ord(str[i])]+=1
    maxl=0
    for i in range(256):
        if count[i]!=0:
            maxl=maxl+1
    return maxl

def unique(str):
    n=len(str)
    distinct=max_char(str,n)
    minl=n
    for i in range(n):
        for j in range(n):
            s=str[i:j]
            s_length = len(s) 
            s1 = max_char(s,s_length) 
              if (s_length < minl and distinct==s1): 
                minl = s_length 
  
    return minl 
    
    
str=input()
l=unique(str)
print(l)
